#!/bin/bash

# Definir variables de entorno para .NET
export HOME=/root
export DOTNET_CLI_HOME=/root
export XDG_DATA_HOME=/root/.local/share

# Actualizar sistema e instalar dependencias
yum update -y
rpm -Uvh https://packages.microsoft.com/config/centos/7/packages-microsoft-prod.rpm
yum install -y dotnet-sdk-8.0 nginx git postgresql15

# Crear directorios para la aplicación
mkdir -p /var/www/chatservice
mkdir -p /var/log/chatservice
chown -R ec2-user:ec2-user /var/www/chatservice
chown -R ec2-user:ec2-user /var/log/chatservice

# Parar servicios si están corriendo
sudo pkill -f dotnet || true
systemctl stop nginx || true

# Descargar y compilar aplicación desde GitHub
cd /tmp
rm -rf AWS_ChatService_.NET8
git clone https://github.com/TheNefelin/AWS_ChatService_.NET8.git
cd AWS_ChatService_.NET8

dotnet restore
dotnet publish AWS_ChatService_API/AWS_ChatService_API.csproj -c Release -o /tmp/published-app

# Hacer backup de aplicación actual si existe
if [ -d "/var/www/chatservice/current" ]; then
    cp -r /var/www/chatservice/current /var/www/chatservice/backup-$(date +%Y%m%d-%H%M%S)
fi

# Desplegar nueva aplicación
rm -rf /var/www/chatservice/current
mkdir -p /var/www/chatservice/current
cp -r /tmp/published-app/* /var/www/chatservice/current/
chown -R ec2-user:ec2-user /var/www/chatservice/current

# Configurar Nginx como reverse proxy
cat > /etc/nginx/conf.d/chatservice.conf << 'EOF'
server {
    listen 80;
    server_name _;
    
    # Configuración de logs
    access_log /var/log/nginx/chatservice_access.log;
    error_log /var/log/nginx/chatservice_error.log;
    
    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection keep-alive;
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Real-IP $remote_addr;
        
        # Timeouts
        proxy_connect_timeout 60s;
        proxy_send_timeout 60s;
        proxy_read_timeout 60s;
    }
    
    # Health check endpoint directo desde nginx
    location /nginx-health {
        access_log off;
        return 200 "nginx healthy\n";
        add_header Content-Type text/plain;
    }
    
    # Archivos estáticos (si los hay)
    location /static/ {
        alias /var/www/chatservice/current/wwwroot/;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }
}
EOF

# Remover configuración default de nginx
rm -f /etc/nginx/conf.d/default.conf
rm -f /etc/nginx/sites-enabled/default

# Crear servicio systemd para la aplicación .NET
cat > /etc/systemd/system/chatservice.service << 'EOF'
[Unit]
Description=Chat Service API (.NET 8)
After=network.target

[Service]
Type=simple
User=ec2-user
Group=ec2-user
WorkingDirectory=/var/www/chatservice/current
ExecStart=/usr/bin/dotnet AWS_ChatService_API.dll
Restart=on-failure
RestartSec=5
KillSignal=SIGINT
SyslogIdentifier=chatservice
Environment=ASPNETCORE_ENVIRONMENT=Production
Environment=ASPNETCORE_URLS=http://0.0.0.0:5000
Environment=DOTNET_PRINT_TELEMETRY_MESSAGE=false
Environment=DB_HOST=TU_RDS_ENDPOINT
Environment=DB_PORT=5432
Environment=DB_NAME=postgres
Environment=DB_USER=postgres
Environment=DB_PASSWORD=TU_PASSWORD
Environment=JWT_SECRET=TU_JWT_SECRET_LARGO_Y_SEGURO

# Logs
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
EOF

# Recargar systemd y habilitar servicios
systemctl daemon-reload
systemctl enable chatservice
systemctl enable nginx

# Iniciar servicios
systemctl start nginx
systemctl start chatservice

# Esperar un momento para que los servicios inicien
sleep 10

# Verificar estado de los servicios
systemctl status nginx --no-pager -l
systemctl status chatservice --no-pager -l

# Limpiar archivos temporales
cd /tmp
rm -rf AWS_ChatService_.NET8 published-app

# Configurar firewall básico si existe
if command -v firewall-cmd &> /dev/null; then
    firewall-cmd --permanent --add-service=http
    firewall-cmd --reload
fi