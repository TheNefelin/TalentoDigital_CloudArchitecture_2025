# Evaluación del Módulo 7 - Microservicios Orquestados

## 📋 Resumen del Proyecto

### Situación Inicial
El sistema monolítico actual de la fintech **MicroPay** presenta problemas de agilidad y escalabilidad. Se decide migrar a una arquitectura de microservicios orquestados en AWS.

### Objetivo
Diseñar e implementar una arquitectura basada en microservicios con:
- Contenedores Docker y orquestación con Kubernetes (EKS).
- API Gateway con autenticación JWT.
- Service Discovery, Circuit Breaker y mensajería asíncrona.
- Alta disponibilidad, escalabilidad y resiliencia.

### Producto Esperado
- Microservicios desplegados en EKS.
- API Gateway con autenticación JWT.
- Uso de AWS Cloud Map, Resilience4j, SNS y SQS.
- Diagrama en Cloudcraft con estimación de costos.
- Documentación con evidencias de TDD, pruebas y refactorizaciones.

---

## ✅ Requerimientos Técnicos

| Componente              | Tecnología/Tool       |
|-------------------------|-----------------------|
| Contenedores            | Docker + Amazon ECR   |
| Orquestación            | Amazon EKS            |
| API Gateway             | AWS API Gateway       |
| Service Discovery       | AWS Cloud Map         |
| Circuit Breaker         | Resilience4j          |
| Mensajería              | SNS + SQS             |
| Diagrama                | Cloudcraft            |
| Pruebas                 | JUnit 5 + JaCoCo      |
| Mocking                 | Mockito               |

---

## 📊 Métricas a Cumplir

| Métrica                  | Mínimo | Máximo |
|--------------------------|--------|--------|
| Funcionalidades CRUD     | 4      | 5      |
| Tests unitarios          | 8      | 16     |
| Cobertura JaCoCo         | 80%    | -      |
| Ciclos TDD               | 12     | -      |
| Refactorizaciones        | 3      | 5      |
| Dependencias mockeadas   | 1      | -      |

---

## 🧩 Paso a Paso por Lección

### Lección 1: Fundamentos de Microservicios y TDD
- ✅ Instalar herramientas: VS Code, JDK 17, JUnit 5, JaCoCo.
- ✅ Crear estructura de proyecto para microservicio de Usuarios.
- ✅ Iniciar repositorio Git.
- ✅ Realizar al menos 1 ciclo TDD (commit RED).
- ✅ Documentar primera prueba RED.

### Lección 2: Patrones Arquitectónicos Clave
- ✅ Implementar API Gateway con autenticación JWT.
- ✅ Configurar AWS Cloud Map.
- ✅ Integrar Circuit Breaker con Resilience4j en microservicio de Pagos.
- ✅ Crear pruebas unitarias con Mockito para capa de seguridad.

### Lección 3: Orquestación con Kubernetes (EKS)
- ✅ Crear Dockerfiles y subir imágenes a ECR.
- ✅ Aprovisionar cluster EKS con eksctl (3 nodos, 2 AZ).
- ✅ Definir Pods, Services y Deployments en YAML.
- ✅ Configurar HPA e Ingress Controller.
- ✅ Capturar métricas de CPU y escalado.

### Lección 4: Representación Cloud y Costos
- ✅ Diagramar arquitectura en Cloudcraft:
  - VPC y subredes.
  - EKS, API Gateway, bases de datos.
  - SNS, SQS, Cloud Map.
- ✅ Etiquetar microservicios y subredes.
- ✅ Calcular costo mensual estimado.
- ✅ Exportar diagrama y añadir al documento Word.

---

## ✅ Checklist Final

- [ ] Microservicios en EKS con auto-escalado.
- [ ] Patrones aplicados: API Gateway, JWT, Service Discovery, Circuit Breaker.
- [ ] Métricas de CRUD, pruebas, TDD y refactor cumplidas.
- [ ] Documentación clara con capturas.
- [ ] Diagrama Cloudcraft y costos justificados.
- [ ] Buenas prácticas de seguridad y resiliencia.

---

# Desarrollo Paso a Paso

```Mermaid
sequenceDiagram
    participant User as Usuario
    participant App as Tu API Gateway
    participant Lambda as Tu Lambda
    participant Cognito

    User->>App: POST /api/signup {email, password}
    App->>Lambda: Invoca función
    Lambda->>Cognito: cognito-idp.sign_up()
    Cognito-->>Lambda: Usuario creado
    Lambda-->>User: {message: "Usuario registrado"}
```

## **Seciruty Group**:
### micropay-sg-rds
- **Name**: micropay-sg-rds
- **Description**: Acceso RDS
- **VPC**: default
- **Inbound rules**:
  - PostgreSQL
    - Type: PostgreSQL
    - Protocol: TCP
    - Port range: 5432
    - Destination type: Anywhere-IPv4
    - Destination: 0.0.0.0/0
    - Description: Acceso PostgreSQL
- **Outbound rules**:
  - Outbound
    - Type: PostgreSQL
    - Protocol: TCP
    - Port range: 5432
    - Destination type: Anywhere-IPv4
    - Destination: 0.0.0.0/0
    - Description: Acceso PostgreSQL

---

## **RDS**: Relational Database Service
### PostgreSQL
- **Creation method**: Standard create
- **Engine type**: PostgreSQL
- **Templates**: Sandbox
- **Availability and durability**: Single-AZ DB instance deployment (1 instance)
- **DB instance**: micropay-rds-pgdb
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
- **Public access**: Yes
- **Security groups**: micropay-sg-rds
- **Monitoring**: Database Insights - Standard
- **Enhanced Monitoring**: Disabled  

---

## **ECR**: Elastic Container Registry
### Repositorio - auth-service-repo
- **Repository name**: micropay-repo
- **Image tag mutability**: Mutable
- **Mutable tag exclusions**:
- **Encryption configuration**: AES-256
- **View push commands**

> [!CAUTION]
> View push commands from `micropay-repo`.

### Repositorio - products-service-repo
- **Repository name**: products-service-repo
- **Image tag mutability**: Mutable
- **Mutable tag exclusions**:
- **Encryption configuration**: AES-256
- **View push commands**

> [!CAUTION]
> View push commands from `products-service-repo`.

### Repositorio - orders-service-repo
- **Repository name**: orders-service-repo
- **Image tag mutability**: Mutable
- **Mutable tag exclusions**:
- **Encryption configuration**: AES-256
- **View push commands**

> [!CAUTION]
> View push commands from `orders-service-repo`.

---

## **EKS**: Elastic Kubernetes Service
### Clusters
- **Configuration options**: Custom configuration
- **Use EKS Auto Mode**_ uncheck
- **Name**: micropay
- **Cluster IAM role**: LabEksClusterRole
- **EKS API**: check
- **ARC Zonal shift**: disabled
- **VPC**: default
- **Subnets**: default
- **Additional security groups**: node-sg-service
- **Cluster endpoint access**: Public and private

### Clusters - Compute - Add node group
- **Name**: ng-general
- **Node IAM role**: LabRole
- **AMI type**: Amazon Linux 2023 (x86_64)
- **Instance types**: t3.medium
- **Disk size**: 20 GiB
- **Desired size**: 2
- **Minimum size**: 2
- **Maximum size**: 4
- **Subnets** default

### Clusters - Resources - Workload ???

---

## **Cognito**:
### Create user pool
- **Application type**: Machine-to-machine application
- **Name**: micropay-cognito

### Cognito - User - Create user 
- ****: 

## **Lambda**
```python
# Ejemplo con Lambda
import boto3

def sign_up(email, password):
    client = boto3.client('cognito-idp')
    
    response = client.sign_up(
        ClientId='13enhv5gkufif0d956a688fb5k',
        Username=email,
        Password=password,
        UserAttributes=[
            {'Name': 'email', 'Value': email}
        ]
    )
    return response
```

---

## **Api Gateway**:
### HTTP API - add Clouster - API server endpoint
- **API name**: micropay-api-gateway
  - **Integrations**:
    - HTTP
    - Method: GET
    - URL endpoint: https:// + user-microservice-LoadBalancer-External-IP + :3000
- **Configure routes**:
  - User
    - **Method**: GET
    - **Resource path**: /User
    - **Integration target**: URL endpoint User

---

## **ServiceDiscovery**: AWSCloudMap

---

## **CircuitBreaker**:

---

## **SQS**: Simple Queue Service:
### Create queue
- **Type**: Standard
- **Name**: monolitica-sqs
- **Visibility timeout**: 30 Seconds
- **Message retention period**: 4 Days
- **Delivery delay**: 0
- **Receive message wait time**: 0
- **Maximum message size**: 1024 KiB

---

## **SNS**: Simple Notification Service 
### Topics
- **Topics**: Standard
- **Name**: monolitica-sns

### Create subscription
- **Topic ARN**: monolitica-sns
- **Protocol**: Amazon SQS
- **Endpoint**: monolitica-sqs

---
