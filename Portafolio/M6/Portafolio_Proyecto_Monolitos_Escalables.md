# Proyecto: Monolitos Escalables en AWS con .NET 8

## 📍 Situación inicial

Actualmente, la aplicación monolítica corre en un único servidor
on-premise, lo que provoca caídas en picos de tráfico y altos costos de
mantenimiento.\
La meta es migrar esta aplicación a **AWS Academy**, manteniendo el
enfoque monolítico pero asegurando **escalabilidad, disponibilidad y
monitoreo**.

------------------------------------------------------------------------

## 📋 Objetivo

Diseñar e implementar una arquitectura monolítica escalable en **AWS**,
aplicando:\
- Balanceo de carga (ELB).\
- Auto Scaling Groups en EC2.\
- Contenerización con Docker y ECR.\
- Mensajería asíncrona con SNS y SQS.\
- Monitoreo y buenas prácticas de infraestructura.

------------------------------------------------------------------------

## 🛠 Producto esperado

1.  Aplicación .NET 8 desplegada en EC2 con **ASG + ELB**.\
2.  Base de datos en **RDS (MySQL o PostgreSQL)** dentro de los límites
    de Academy.\
3.  Dockerfile y push de la imagen a **ECR**. (Opcional: despliegue
    ECS/Fargate).\
4.  Integración de **SNS (notificaciones)** y **SQS (procesamiento
    asíncrono)**.\
5.  Diagrama en **Cloudcraft** con costos estimados (AWS Pricing
    Calculator).

------------------------------------------------------------------------

## 🤝🏻 Requerimientos (adaptados a AWS Academy)

-   ✅ **EC2**: instancias `t2.micro` o `t3.micro` para pruebas, con
    ASG.\
-   ✅ **RDS**: MySQL/Postgres con máximo **100 GB gp2** (limitación
    Academy).\
-   ✅ **ECR + Docker**: crear repositorio y subir imagen de .NET 8.\
-   ✅ **SNS y SQS**: simular notificaciones y colas de procesamiento.\
-   ✅ **VPC y subredes**: usar configuración estándar Academy (evitar
    NAT Gateway por costo).\
-   ✅ **Cloudcraft**: generar diagrama y costos mensuales (mínimos).

------------------------------------------------------------------------

## 🔢 Métricas Generales

-   CRUD: 4 entidades (ejemplo: `Usuarios`, `Productos`, `Pedidos`,
    `Facturas`).\
-   Tests unitarios: 10 en total, con **xUnit o NUnit en .NET**.\
-   Cobertura: usar `coverlet` con mínimo 80%.\
-   TDD: al menos 12 ciclos RED-GREEN-REFACTOR.\
-   Refactorizaciones: 3--5.\
-   Mockito → En .NET usaremos **Moq** para mocking.

------------------------------------------------------------------------

## 👣 Paso a paso (resumido con respuestas)

### Lección 1 -- Fundamentos de Escalabilidad y TDD

-   Instalar **.NET 8 SDK**, `xUnit`, `coverlet`.\
-   Repo Git creado.\
-   Primer test `RED` implementado (ejemplo: validar creación de
    usuario).

### Lección 2 -- Implementación Monolítica en la Nube

-   Crear instancia EC2 (`t3.micro`).\
-   Crear RDS (MySQL 8).\
-   Deploy app con `dotnet publish` y configurar cadena de conexión.

### Lección 3 -- Escalabilidad y Alta Disponibilidad

-   Configurar **ASG basado en CPU \> 70%**.\
-   Crear **Application Load Balancer** para balanceo de tráfico.

### Lección 4 -- Contenerización con Docker

-   Crear `Dockerfile`:

    ``` dockerfile
    FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS base
    WORKDIR /app
    COPY . .
    ENTRYPOINT ["dotnet", "App.dll"]
    ```

-   Subir imagen a **ECR**.\

-   (Opcional) Comparar despliegue en ECS/Fargate (limitado en Academy).

### Lección 5 -- Servicios de Mensajería

-   Crear **SNS Topic** para notificaciones.\
-   Crear **SQS Queue** y suscripción desde SNS.\
-   Probar envío de mensajes desde app .NET con `AWSSDK.SQS`.

### Lección 6 -- Representación Cloud

-   Diagramar en **Cloudcraft**:
    -   VPC con 2 subredes públicas + 2 privadas.\
    -   EC2 en ASG con ALB.\
    -   RDS en subred privada.\
    -   ECR, SNS, SQS.\
-   Calcular costos (\~10--15 USD/mes usando Academy límites).

------------------------------------------------------------------------

## 🔍 Validación

-   Uso de servicios AWS permitido en Academy.\
-   Cumplimiento de métricas (CRUD, TDD, pruebas).\
-   Documentación clara con capturas.\
-   Diagrama Cloudcraft coherente y económico.

------------------------------------------------------------------------

# Desarrollo Paso a Paso

- [Repo GitHub](https://github.com/TheNefelin/AWS_ApiSNS_WorkerSQS_.NET8)

```
Usuario -> (POST Pedido) -> Monolito .NET (EC2 + Docker)
    |
    |---> Guarda en RDS
    |
    |---> Publica evento "DonacionCreado" en SNS
                 |
                 +--> Notificación email (subscripción)
                 +--> Notificación email (desubscripción)
                 +--> Notificación email (donacion)            
                 +--> Cola SQS "Facturacion"
                          |
                          +--> Worker .NET procesa facturación (en segundo plano)
                          +--> Actualiza stock en RDS
                          +--> Notificación email (factura) 
```

---

## **Seciruty Group**:
### monolito-sg-rds
- **Name**: monolito-sg-rds
- **Description**: Acceso RDS
- **VPC**: default
- **Inbound rules**:
  - PostgreSQL
    - Type: PostgreSQL
    - Protocol: TCP
    - Port range: 5432
    - Destination type: Custom
    - Destination: 0.0.0.0/0
    - Description: Acceso PostgreSQL
- **Outbound rules**:
  - Outbound
    - Type: PostgreSQL
    - Protocol: TCP
    - Port range: 5432
    - Destination type: Custom
    - Destination: 0.0.0.0/0
    - Description: Acceso PostgreSQL

### webapi-sg
- **Name**: monolito-sg-webapi
- **Description**: Acceso WebApi
- **VPC**: default
- **Inbound rules**:
  - SSH
    - Type: SSH
    - Protocol: TCP
    - Port range: 22
    - Destination type: Anywhere-IPv4
    - Destination: 0.0.0.0/0
    - Description: Acceso SSH
  - HTTP
    - Type: HTTP
    - Protocol: TCP
    - Port range: 80
    - Destination type: Anywhere-IPv4
    - Destination: 0.0.0.0/0
    - Description: Acceso web    
- **Outbound rules**:
  - Outbound
    - Type: All traffic
    - Protocol: all
    - Port range: all
    - Destination type: Custom
    - Destination: 0.0.0.0/0
    - Description:

---

## **S3 Bucket**: Almacenamiento Estático
### Bucket
- **Name**: monolito-storage
- **Object Ownership**: ACLs desactivados
- **Block all public access**: check
- **Versioning**: Disable
- **Encryption**: SSE-S3
- **Bucket Key**: Disable

```bash
monolito-storage/
├── docs/
└── images/
```

---

## **RDS**: Relational Database Service
### PostgreSQL
- **Creation method**: Standard create
- **Engine type**: PostgreSQL
- **Templates**: Dev/Test
- **Availability and durability**: Multi-AZ DB instance deployment (2 instances)
- **DB instance**: monolito-pgdb
- **Master username**: postgres
- **Credentials management**: ********
- **Instance configuration**:
    - Burstable classes (includes t classes)
    - db.t3.micro
- **Allocated storage**: 20 GiB
- **Enable storage autoscaling**: check
- **Compute resource**: Don’t connect to an EC2 compute resource
- **VPC**: default
- **DB subnet group**: default
- **Public access**: yes
- **Security groups**: monolito-sg-rds
- **Monitoring**: Database Insights - Standard
- **Enhanced Monitoring**: Disabled  

```sql
CREATE TABLE Companies (
    company_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    img TEXT
);

INSERT INTO Companies 
    (name, email, img) 
VALUES
    ('Weyland-Yutani', 'info@wy.com', 'wy.webp'),
    ('Omni Consumer Products', 'info@ocp.com', 'ocp.webp'),
    ('Cyberdyne Systems Corporation', 'info@csc.com', 'csc.webp'),
    ('Umbrella Corporation', 'info@uc.com', 'uc.webp');
```

```sql
CREATE TABLE Products (
    product_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    price INT NOT NULL
);

INSERT INTO Products 
	(name, description, price) 
VALUES
	('Réplica del Cargador de Montacargas P-5000', '', 55000),
	('Set de Miniaturas Coleccionables de Xenomorfos', '', 18000),
	('Figura de Acción de un Sintético con Daños de Batalla', '', 29990),
	('Vehículo de Patrulla OCP con Luces y Sonido', '', 22000),
	('Figura de RoboCop "Ultimate Edition"', '', 45000),
	('Set de Construcción "Torre ED-209"', '', 68000),
	('Figura de Acción del T-800 Endoskeleton', '', 35000),
	('Cabeza de Colección de un T-1000 de Metal Líquido', '', 75000),
	('Réplica del Computador de Skynet', '', 50000),
	('Figura de Acción del T-Virus Zombie', '', 28000),
	('Set de Laboratorio Secreto de Umbrella', '', 60000),
	('Réplica de la Vacuna Anti-Virus', '', 15000);

SELECT * FROM Products;
```

---

## **SQS**: Simple Queue Service:
### Create queue
- **Type**: Standard
- **Name**: monolito-sqs-worker
- **Visibility timeout**: 30 Seconds
- **Message retention period**: 4 Days
- **Delivery delay**: 0
- **Receive message wait time**: 0
- **Maximum message size**: 1024 KiB

> Obtener URL para la variable de entorno

---

## **SNS**: Simple Notification Service 
### Topics
- **Topics**: Standard
- **Name**: monolito-sns-webapi

### Create subscription
- **Topic ARN**: monolito-sns-webapi
- **Protocol**: Amazon SQS
- **Endpoint**: monolito-sqs-worker

> Obtener ARN para la variable de entorno

---

## Desplegar WebApi + Worker (SNS + SQS)
- Opcion 1: 
    - **EB**: Elastic Beanstalk
- Opcion 2: 
    - **CloudShell**
    - **ECR**: Elastic Container Registry 
    - **ECS**: Elastic Container Service

---

## Opcion 1: **EB**
### WebApi
- **Environment tier**: Web server environment
- **Application name**: monolito-eb-webapi
- **Platform**: .NET Core on Linux
- **Platform branch**: .NET 8 running on 64bit Amazon Linux 2023
- **Platform version**: 3.5.4
- **Upload your code**: check
- **Version labe**: 1
- **Local file**: AWS_SNS_WebApi.zip
- **Single instance**: check
- **Service role**: LabRole
- **EC2 instance profile**: LabInstanceProfile
- **EC2 key pair**: vockey
- **VPC**: default
- **Public IP address**: Enable
- **Instance subnets**:
  - us-east-1a
  - us-east-1b
- **EC2 security groups**: monolito-sg-webapi
- **Health reporting**: Basic
- **Managed updates**: uncheck
- **Environment properties**:
  - Region
    - **Name**: AWS_REGION
    - **Value**: us-east-1
  - SNS
    - **Name**: SNS_TOPIC_ARN
    - **Value**: arn:aws:sns:us-east-1:123:monolitica-sns
  - RDS Host
    - **Name**: DB_HOST
    - **Value**: monolito-pgdb.123.us-east-1.rds.amazonaws.com
  - RDS Port
    - **Name**: DB_PORT
    - **Value**: 5432
  - RDS Name
    - **Name**: DB_NAME
    - **Value**: postgres
  - RDS User
    - **Name**: DB_USER
    - **Value**: postgres    
  - RDS Password
    - **Name**: DB_PASSWORD
    - **Value**: ****

### WebApi
- **Environment tier**: Web server environment
- **Application name**: monolito-eb-worker
...

---
