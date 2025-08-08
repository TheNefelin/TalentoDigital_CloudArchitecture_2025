sudo su

# Verificar instalación
dotnet --version
systemctl restart nginx

# Test local
curl -s http://localhost/ || echo "❌ No responde"
curl -s http://localhost/health || echo "❌ Health check falla"

# Clonar de GitHub
ps aux | grep dotnet
kill 21746
cd /var/www/artema-api
rm -rf *
git clone https://github.com/TheNefelin/AWS_ChatService_.NET8.git
cd AWS_ChatService_.NET8
dotnet restore
cd AWS_ChatService_API
dotnet build
nohup dotnet run --urls "http://0.0.0.0:5000" > /var/log/artema-api/artema-api.log 2>&1 &

nano appsettings.json
# Ctrl + O para guardar 
# Ctrl + X para salir

###############################################

#!/bin/bash

# Definir HOME para que .NET funcione
export HOME=/root
export DOTNET_CLI_HOME=/root
export XDG_DATA_HOME=/root/.local/share

yum update -y

# Amazon Linux necesita este repositorio para .NET
rpm -Uvh https://packages.microsoft.com/config/centos/7/packages-microsoft-prod.rpm
# Instalar .NET 8, nginx, git y PostgreSQL client
yum install -y dotnet-sdk-8.0 nginx git postgresql15

# Crear directorios para la aplicación
mkdir -p /var/www/artema-api
mkdir -p /var/log/artema-api
chown -R ec2-user:ec2-user /var/www/artema-api
chown -R ec2-user:ec2-user /var/log/artema-api

# Configurar Nginx como reverse proxy
cat > /etc/nginx/conf.d/artema-api.conf << 'EOF'
server {
    listen 80;
    server_name _;
    
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
    }
    
    # Health check endpoint
    location /health {
        access_log off;
        return 200 "healthy\n";
        add_header Content-Type text/plain;
    }
}
EOF

# Remover/limpiar configuración default de nginx
rm -f /etc/nginx/conf.d/default.conf

# Habilitar y iniciar servicios
systemctl enable nginx
systemctl start nginx

# Ir al directorio de la aplicación
cd /var/www/artema-api
# Crear proyecto .NET 8 Web API
dotnet new webapi -n ArtemaChatApi

# Ir al directorio del proyecto
cd ArtemaChatApi
# Editar el archivo Program.cs para que escuche en todas las interfaces
cat > Program.cs << 'EOF'
var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddControllers();
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseRouting();
app.UseAuthorization();
app.MapControllers();

// Endpoints de prueba
app.MapGet("/", () => "Artema Chat API - Version 1.0 🚀");
app.MapGet("/health", () => "API is running!");
app.MapGet("/info", () => new { 
    version = "1.0", 
    timestamp = DateTime.Now,
    environment = Environment.GetEnvironmentVariable("ASPNETCORE_ENVIRONMENT") ?? "Production"
});

// CRÍTICO: Escuchar en todas las interfaces
app.Run("http://0.0.0.0:5000");
EOF

# Compilar y ejecutar
dotnet build
dotnet run
