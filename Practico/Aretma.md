# AWS Artema Aplicación .NET 8 + Angular 20 + PostgreSQL

## Diagrama

<img src="..\Img\Artema.drawio.png">

---

## **1. VPC: Virtual Private Cloud**
### artema-vpc
- **VPC settings**: VPC and more
- **Name**: artema
- **IPv4 CIDR block**: 10.0.0.0/16
- **IPv6 CIDR block**: No IPv6 CIDR block
- **Tenancy**: Default
- **Number of Availability Zones**: 2
- **Customize AZs**:
  - us-east-1a
  - us-east-1b
- **Number of public subnets**: 2
- **Number of private subnets**: 2
- **Customize subnets CIDR blocks**:
  - Public subnet CIDR block in us-east-1a: 10.0.0.0/20
  - Public subnet CIDR block in us-east-1b: 10.0.16.0/20
  - Private subnet CIDR block in us-east-1a: 10.0.128.0/20
  - Private subnet CIDR block in us-east-1b: 10.0.144.0/20
- **NAT gateways**: In 1 AZ
- **VPC endpoints**: None
- **Enable DNS hostnames**: Check
- **Enable DNS resolution**: Check

### Enrutar subredes privadas por un solo camino
```
Route tables
└── artema-rtb-private1-us-east-1a to rename ==> artema-rtb-private
    └── Subnet associations
        └── Edit subnet associations
            ├── Selected subnets
            │   ├── artema-subnet-private1-us-east-1a     
            │   └── artema-subnet-private2-us-east-1b
            └── Save associations
```

```
Router Table
    ├── artema-rtb-public
    │   ├── Routes
    │   │   ├── igw 0.0.0.0/0
    │   │   └── local 10.0.0.0/16
    │   └── Subnet associations
    │       ├── artema-subnet-public1-us-east-1a 10.0.0.0/20
    │       └── artema-subnet-public2-us-east-1b 10.0.16.0/20
    └── artema-rtb-private
        ├── Routes
        │   ├── nat 0.0.0.0/0
        │   └── local 10.0.0.0/16
        └── Subnet associations
            ├── artema-subnet-private1-us-east-1a 10.0.128.0/20
            └── artema-subnet-private2-us-east-1b 10.0.144.0/20    
```

---

## **2. Seciruty Group**: (reglas de seguridad)
### 2.1 artema-sg-bastion
- **Name**: artema-sg-bastion
- **Description**: Acceso SSH y PostgreSQL
- **VPC**: artema-vpc
- **Inbound rules**:
  - SSH
    - Type: SSH
    - Protocol: TCP
    - Port range: 22
    - Destination type: Anywhere-IPv4
    - Destination: 0.0.0.0/0 (MyIP)
    - Description: Acceso SSH
  - HTTP
    - Type: SSH
    - Protocol: TCP
    - Port range: 80
    - Destination type: Anywhere-IPv4
    - Destination: 0.0.0.0/0 (MyIP)
    - Description: Acceso web
  - PostgreSQL (Hacia RDS)
    - Type: PostgreSQL
    - Protocol: TCP
    - Port range: 5432
    - Destination type: Custom
    - Destination: artema-sg-rds
    - Description: Acceso a PostgreSQL artema-sg-rds desde artema-sg-bastion
- **Outbound rules**:
  - Outbound
    - Type: All traffic
    - Protocol: all
    - Port range: all
    - Destination type: Custom
    - Destination: 0.0.0.0/0
    - Description: 

### 2.2 artema-sg-api
- **Name**: artema-sg-api
- **Description**: Acceso HTTP/HTTPS para API
- **VPC**: artema-vpc
- **Inbound rules**:
  - SSH
    - Type: SSH
    - Protocol: TCP
    - Port range: 22
    - Destination type: Anywhere-IPv4
    - Destination: 0.0.0.0/0 (MyIP)
    - Description: Acceso SSH
  - HTTP
    - Type: SSH
    - Protocol: TCP
    - Port range: 80
    - Destination type: Anywhere-IPv4
    - Destination: 0.0.0.0/0 (MyIP)
    - Description: Acceso HTTP a la API
  - HTTPS
    - Type: SSH
    - Protocol: TCP
    - Port range: 443
    - Destination type: Anywhere-IPv4
    - Destination: 0.0.0.0/0 (MyIP)
    - Description: Acceso HTTPS a la API   
  - PostgreSQL (Hacia RDS)
    - Type: PostgreSQL
    - Protocol: TCP
    - Port range: 5432
    - Destination type: Custom
    - Destination: artema-sg-rds
    - Description: Acceso a PostgreSQL artema-sg-rds desde artema-sg-api
- **Outbound rules**:
  - Outbound
    - Type: All traffic
    - Protocol: all
    - Port range: all
    - Destination type: Custom
    - Destination: 0.0.0.0/0
    - Description:

### 2.3 artema-sg-rds
- **Name**: artema-sg-rds
- **Description**: Acceso a PostgreSQL
- **VPC**: artema-vpc
- **Inbound rules**:
  - PostgreSQL (Desde Bastion)
    - Type: PostgreSQL
    - Protocol: TCP
    - Port range: 5432
    - Destination type: Custom
    - Destination: artema-sg-bastion
    - Description: Acceso a PostgreSQL desde artema-sg-bastion
  - PostgreSQL (Desde API)
    - Type: PostgreSQL
    - Protocol: TCP
    - Port range: 5432
    - Destination type: Custom
    - Destination: artema-sg-api
    - Description: Acceso a PostgreSQL desde artema-sg-api    
- **Outbound rules**:
  - Outbound
    - Type: All traffic
    - Protocol: all
    - Port range: all
    - Destination type: Custom
    - Destination: 0.0.0.0/0
    - Description: 

---

### PuTTY
- Session
  - HostName: BastionIP
- Connection
  - Seconds: 30
  - SSH
    - Auth
      - Credentials
        - Private Key: artema-key.ppk
    - Tunnels      
      - Source port: 5433
      - Destination: RDS-Endpoint + : + 5432
### Console
```bash
ec2-user
```

---

## **3. RDS**: Relational Database Service (servicio de base de datos)
### 3.1 DRS Subnet Group
- **Name**: artema-rds-sng
- **Description**: Private subnet group para PostgreSQL
- **VPC**: artema-vpc
- **Availability Zones**:
    - us-east-1a
    - us-east-1b
- **Subnets**:
    - artema-subnet-private1-us-east-1a
    - artema-subnet-private2-us-east-1b

### 3.2 PostgreSQL
- **Creation method**: Standard create
- **Engine type**: PostgreSQL
- **Templates**: Dev/Test
- **Availability and durability**: Multi-AZ DB instance deployment (2 instances)
- **DB instance**: artema-pgdb
- **Master username**: postgres
- **Credentials management**: ********
- **Instance configuration**:
    - Burstable classes (includes t classes)
    - db.t3.micro
- **Allocated storage**: 20 GiB
- **Compute resource**: Don’t connect to an EC2 compute resource
- **Network type**: IPv4
- **VPC**: artema-vpc
- **DB subnet group**: artema-rds-sng
- **Public access**: No
- **Security groups**: artema-sg-rds
- **Enhanced Monitoring**: Disabled  

```sql
CREATE TABLE IF NOT EXISTS Users (
    Id UUID PRIMARY KEY,
    Username TEXT NOT NULL,
    ConnectedAt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS ChatRooms (
    Id UUID PRIMARY KEY,
    Name TEXT NOT NULL,
    CreatedAt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS Messages (
    Id UUID PRIMARY KEY,
    Content TEXT NOT NULL,
    SentAt TIMESTAMP NOT NULL,
    UserId UUID NOT NULL REFERENCES Users(Id),
    ChatRoomId UUID NOT NULL REFERENCES ChatRooms(Id)
);

INSERT INTO Users (Id, Username, ConnectedAt)
VALUES ('11112222-3333-4444-5555-666677778888', 'Usuario de Prueba', CURRENT_TIMESTAMP);

INSERT INTO ChatRooms (Id, Name, CreatedAt)
VALUES ('11112222-3333-4444-5555-666677778888', 'Sala de Prueba', CURRENT_TIMESTAMP);

INSERT INTO Messages 
    (Id, Content, SentAt, UserId, ChatRoomId)
VALUES
    ('11111111-3333-4444-5555-666677778888', '¡Hola desde REST!', CURRENT_TIMESTAMP, '11112222-3333-4444-5555-666677778888', '11112222-3333-4444-5555-666677778888'),
    ('22222222-3333-4444-5555-666677778888', 'Mensaje de prueba desde la API', CURRENT_TIMESTAMP, '11112222-3333-4444-5555-666677778888', '11112222-3333-4444-5555-666677778888');

SELECT * FROM Users;  
SELECT * FROM ChatRooms;  
SELECT * FROM Messages;    
```

---

## **4. EC2**: Launch Templates
### 4.1 Launch template Bastion
- **Name**: artema-lt-bastion
- **Description**: Plantilla base para bastion
- **OS Images**: Amazon Linux
- **Amazon Machine Image**: Amazon Linux 2023 kernel-6.1 AMI
- **Instance type**: t2.nano
- **Key pair**: artema-key.ppk (RSA) (.ppk)
- **Subnet**: Don't include in launch template
- **Availability Zone**: Don't include in launch template
- **security groups**: artema-sg-firewall
- **Advanced network configuration**:
  - **Auto-assign public IP**: Enable
- **Resource tags**
  - **Key**: Name
  - **Value**: artema-ec2-bastion
  - **Resource types**: Instances
- **Advanced details**:
  - **IAM instance profile**: LabInstanceProfile
  - **User data**
```bash
#!/bin/bash
yum install -y httpd
systemctl enable httpd
systemctl start httpd
echo '<html><h1>EC2 Bastion Corriendo!!!</h1></html>' > /var/www/html/index.html
yum update && yum upgrade -y
```

### Launch instance from template
- **Source template**: artema-lt-bastion
- **Subnet**: artema-subnet-public1-us-east-1a
- **Availability Zone**: us-east-1a

### 4.2 Launch template API .NET 8
- **Name**: artema-lt-api-dotnet8
- **Description**: Plantilla para API .NET 8
- **OS Images**: Amazon Linux
- **Amazon Machine Image**: Amazon Linux 2023 kernel-6.1 AMI
- **Instance type**: t3.nano
- **Key pair**: artema-key.ppk (RSA) (.ppk)
- **Subnet**: Don't include in launch template
- **Availability Zone**: Don't include in launch template
- **security groups**: artema-sg-api
- **Advanced network configuration**:
  - **Auto-assign public IP**: Enable
- **Resource tags**
  - **Key**: Name
  - **Value**: artema-ec2-dotnet8
  - **Resource types**: Instances
- **Advanced details**:
  - **IAM instance profile**: LabInstanceProfile
  - **User data**
```bash
#!/bin/bash
export HOME=/root
export DOTNET_CLI_HOME=/root
export XDG_DATA_HOME=/root/.local/share

yum update -y

rpm -Uvh https://packages.microsoft.com/config/centos/7/packages-microsoft-prod.rpm
yum install -y dotnet-sdk-8.0 nginx git postgresql15

mkdir -p /var/www/artema-api
mkdir -p /var/log/artema-api
chown -R ec2-user:ec2-user /var/www/artema-api
chown -R ec2-user:ec2-user /var/log/artema-api

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

rm -f /etc/nginx/conf.d/default.conf

systemctl enable nginx
systemctl start nginx

cd /var/www/artema-api
dotnet new webapi -n ArtemaChatApi

cd ArtemaChatApi
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

dotnet build
dotnet run
```

### Clonar GitHub
```bash
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
```

### 4.3 EC2 Docker
```bash
yum update -y
dnf install -y docker
systemctl start docker
systemctl enable docker
usermod -a -G docker ec2-user
newgrp docker
docker --version
```

---

## **ECR**: Amazon Elastic Container Registry
> [!CAUTION] No Disponible

### Create private repository
- **Repository name**: artema-chat
- **Mutable**: check
- **AES-256**: check

### IAM Users: 
- **Name**: artema-deploy-user
- **Permissions policies**: AmazonEC2ContainerRegistryPowerUser

### 5.3 Instalar AWS CLI en Windows
- [AWS CLI Installer (Windows 64-bit)](https://awscli.amazonaws.com/AWSCLIV2.msi)
- [Doc oficial](https://docs.aws.amazon.com/es_es/cli/latest/userguide/getting-started-install.html)
```bash
aws --version
aws configure
```

### Desde PowerShell local (con Docker Desktop corriendo)
- View push commands
```bash
# Autentica Docker en AWS ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 527237860774.dkr.ecr.us-east-1.amazonaws.com

# Etiqueta tu imagen con la URI de ECR
docker tag artema-chat-app:latest 527237860774.dkr.ecr.us-east-1.amazonaws.com/artema-chat:latest

# Sube la imagen
docker push 527237860774.dkr.ecr.us-east-1.amazonaws.com/artema-chat:latest
```

### Desde EC2
```bash
# Autentica el EC2 en ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 527237860774.dkr.ecr.us-east-1.amazonaws.com

# Descarga la imagen
docker pull 527237860774.dkr.ecr.us-east-1.amazonaws.com/artema-chat:latest
```

---












```
GitHub (Repositorio)
  │
  ▼
AWS CodePipeline (Origen: GitHub, Disparador por cambios)
  │
  ▼
AWS CodeBuild (Build, Test, Publicar artefacto)
  │
  ▼
AWS S3 (Almacenamiento de artefactos)
  │
  ▼
AWS CodeDeploy (Despliegue en EC2)
```
