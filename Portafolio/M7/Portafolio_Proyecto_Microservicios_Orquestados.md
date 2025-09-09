# Evaluación del Módulo 7 - Microservicios Orquestados

## 📋 Resumen del Proyecto

### Situación Inicial
El sistema monolítico actual de la fintech **MicroPay** presenta problemas de agilidad y escalabilidad. Se decide migrar a una arquitectura de microservicios orquestados en AWS.

### Objetivo
Diseñar e implementar una arquitectura basada en microservicios con:
- Contenedores Docker y Orquestación con Kubernetes (EKS).
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

### Flujo real de registro
```Mermaid
sequenceDiagram
    participant User as Usuario
    participant App as API Gateway
    participant Lambda as Lambda
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
    - Type: All traffic
    - Protocol: All
    - Port range: All
    - Destination type: Custom
    - Destination: 0.0.0.0/0
    - Description:

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

## **SQS**: Simple Queue Service:
### Create queue
- **Type**: Standard
- **Name**: micropay-sqs
- **Visibility timeout**: 30 Seconds
- **Message retention period**: 4 Days
- **Delivery delay**: 0
- **Receive message wait time**: 0
- **Maximum message size**: 1024 KiB

---

## **SNS**: Simple Notification Service 
### Topics
- **Topics**: Standard
- **Name**: micropay-sns

### Create subscription
- **Topic ARN**: micropay-sns
- **Protocol**: Amazon SQS
- **Endpoint**: micropay-sqs

---

## **ECR**: Elastic Container Registry
### Repositorio - products-service-repo
- **Repository name**: micropay-repo-notification
- **Image tag mutability**: Mutable
- **Mutable tag exclusions**:
- **Encryption configuration**: AES-256
- **View push commands**

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
- **Additional security groups**: micropay-sg-service
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

### Cognito - User Pool
- User pool ID

### Cognito - App clients - micropay-cognito
- Client ID
- Client secret

### Cognito - App clients - micropay-cognito - edit
- **Sign in with username and password: ALLOW_USER_PASSWORD_AUTH**: check
- **Sign in with server-side administrative credentials: ALLOW_ADMIN_USER_PASSWORD_AUTH**: check

---

## **Lambda**: Auth Register
### Lambda Register
- **Function name**: micropay-lambda-register
- **Runtime**: Python 3.13
- **Architecture**: x86_64
- **Execution role**: LabRole

### Environment variable
- **COGNITO_CLIENT_ID**: COGNITO_CLIENT_ID
- **COGNITO_CLIENT_SECRET**: COGNITO_CLIENT_SECRET
- **COGNITO_USER_POOL_ID**: COGNITO_USER_POOL_ID

```py
import boto3
import json
import os
import hmac
import hashlib
import base64

def calculate_secret_hash(username, client_id, client_secret):
    message = username + client_id
    dig = hmac.new(
        client_secret.encode('utf-8'),
        msg=message.encode('utf-8'),
        digestmod=hashlib.sha256
    ).digest()
    return base64.b64encode(dig).decode()

def lambda_handler(event, context):
    client = boto3.client('cognito-idp')
    
    CLIENT_ID = os.environ['COGNITO_CLIENT_ID']
    CLIENT_SECRET = os.environ['COGNITO_CLIENT_SECRET']
    USER_POOL_ID = os.environ['COGNITO_USER_POOL_ID']
    
    body = json.loads(event['body'])
    email = body['email']
    password = body['password']
    
    secret_hash = calculate_secret_hash(email, CLIENT_ID, CLIENT_SECRET)
    
    try:
        # 1. Registrar usuario
        response = client.sign_up(
            ClientId=CLIENT_ID,
            Username=email,
            Password=password,
            SecretHash=secret_hash,
            UserAttributes=[{'Name': 'email', 'Value': email}]
        )
        
        # 2. ✅ VERIFICAR ADMINISTRATIVAMENTE (sin código)
        client.admin_confirm_sign_up(
            UserPoolId=USER_POOL_ID,
            Username=email
        )
        
        # 3. ✅ MARCAR EMAIL COMO VERIFICADO
        client.admin_update_user_attributes(
            UserPoolId=USER_POOL_ID,
            Username=email,
            UserAttributes=[
                {'Name': 'email_verified', 'Value': 'true'}
            ]
        )
        
        return {
            'statusCode': 200,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({
                'message': 'Usuario registrado y verificado automáticamente',
                'userSub': response['UserSub']
            })
        }
        
    except client.exceptions.UsernameExistsException:
        return {
            'statusCode': 400,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': 'El usuario ya existe'})
        }
    except Exception as e:
        return {
            'statusCode': 400,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': str(e)})
        }
```
```json
{
  "body": "{\"email\": \"test@example.com\", \"password\": \"Password123!\"}",
  "httpMethod": "POST"
}
```
```json
{
  "email": "test@example.com", 
  "password": "Password123!"
}
```

## **Lambda**: Auth Login
### Lambda Login
- **Function name**: micropay-lambda-login
- **Runtime**: Python 3.13
- **Architecture**: x86_64
- **Execution role**: LabRole

### Environment variable
- **COGNITO_CLIENT_ID**: COGNITO_CLIENT_ID
- **COGNITO_CLIENT_SECRET**: COGNITO_CLIENT_SECRET
- **COGNITO_USER_POOL_ID**: COGNITO_USER_POOL_ID

```py
import boto3
import json
import os
import hmac
import hashlib
import base64

# Calcular SECRET_HASH (igual que en registro)
def calculate_secret_hash(username, client_id, client_secret):
    message = username + client_id
    dig = hmac.new(
        client_secret.encode('utf-8'),
        msg=message.encode('utf-8'),
        digestmod=hashlib.sha256
    ).digest()
    return base64.b64encode(dig).decode()

def lambda_handler(event, context):
    client = boto3.client('cognito-idp')
    
    # Obtener configuración desde variables de entorno
    CLIENT_ID = os.environ['COGNITO_CLIENT_ID']
    CLIENT_SECRET = os.environ['COGNITO_CLIENT_SECRET']
    USER_POOL_ID = os.environ['COGNITO_USER_POOL_ID']
    
    try:
        # Parsear el body de la request
        body = json.loads(event['body'])
        email = body['email']
        password = body['password']
        
        # Calcular secret hash (OBLIGATORIO porque tienes Client Secret)
        secret_hash = calculate_secret_hash(email, CLIENT_ID, CLIENT_SECRET)
        
        # Hacer login con Cognito
        response = client.admin_initiate_auth(
            UserPoolId=USER_POOL_ID,
            ClientId=CLIENT_ID,
            AuthFlow='ADMIN_NO_SRP_AUTH',
            AuthParameters={
                'USERNAME': email,
                'PASSWORD': password,
                'SECRET_HASH': secret_hash
            }
        )
        
        # Extraer tokens de la respuesta
        auth_result = response['AuthenticationResult']
        
        # Respuesta exitosa
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'message': 'Login exitoso',
                'access_token': auth_result['AccessToken'],
                'refresh_token': auth_result['RefreshToken'],
                'expires_in': auth_result['ExpiresIn'],
                'token_type': auth_result['TokenType']
            })
        }
        
    except client.exceptions.NotAuthorizedException:
        return {
            'statusCode': 401,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': 'Email o contraseña incorrectos'})
        }
    except client.exceptions.UserNotFoundException:
        return {
            'statusCode': 404,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': 'Usuario no encontrado'})
        }
    except client.exceptions.UserNotConfirmedException:
        return {
            'statusCode': 403,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': 'Usuario no verificado. Revisa tu email para verificar la cuenta.'})
        }
    except json.JSONDecodeError:
        return {
            'statusCode': 400,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': 'Formato de JSON inválido'})
        }
    except KeyError as e:
        return {
            'statusCode': 400,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': f'Falta campo requerido: {str(e)}'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': f'Error interno del servidor: {str(e)}'})
        }
```
```json
{
  "body": "{\"email\": \"test@example.com\", \"password\": \"Password123!\"}",
  "httpMethod": "POST"
}
```
```json
{
  "email": "test@example.com", 
  "password": "Password123!"
}
```

## **Lambda**: Auth logout
### Lambda Register
- **Function name**: micropay-lambda-logout
- **Runtime**: Python 3.13
- **Architecture**: x86_64
- **Execution role**: LabRole

### Environment variable
- **COGNITO_CLIENT_ID**: COGNITO_CLIENT_ID
- **COGNITO_CLIENT_SECRET**: COGNITO_CLIENT_SECRET
- **COGNITO_USER_POOL_ID**: COGNITO_USER_POOL_ID

```py
import boto3
import json
import os
import hmac
import hashlib
import base64

def calculate_secret_hash(username, client_id, client_secret):
    """
    Calcula el SECRET_HASH requerido por Cognito cuando el cliente tiene Client Secret
    """
    message = username + client_id
    dig = hmac.new(
        client_secret.encode('utf-8'),
        msg=message.encode('utf-8'),
        digestmod=hashlib.sha256
    ).digest()
    return base64.b64encode(dig).decode()

def lambda_handler(event, context):
    client = boto3.client('cognito-idp')
    
    # Variables de entorno (las mismas que en login/register)
    CLIENT_ID = os.environ['COGNITO_CLIENT_ID']
    CLIENT_SECRET = os.environ['COGNITO_CLIENT_SECRET']
    USER_POOL_ID = os.environ['COGNITO_USER_POOL_ID']
    
    try:
        # Parsear el body de la request
        body = json.loads(event['body'])
        
        # Opción 1: Logout con email (requiere SECRET_HASH)
        if 'email' in body:
            email = body['email']
            secret_hash = calculate_secret_hash(email, CLIENT_ID, CLIENT_SECRET)
            
            # Logout global del usuario (invalida todos los tokens)
            response = client.admin_user_global_sign_out(
                UserPoolId=USER_POOL_ID,
                Username=email
            )
            
            return {
                'statusCode': 200,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Content-Type': 'application/json'
                },
                'body': json.dumps({
                    'message': 'Logout exitoso. Todos los tokens han sido invalidados.',
                    'method': 'global_sign_out'
                })
            }
        
        # Opción 2: Logout con access_token (más común en frontends)
        elif 'access_token' in body:
            access_token = body['access_token']
            
            # Logout con token específico
            response = client.global_sign_out(
                AccessToken=access_token
            )
            
            return {
                'statusCode': 200,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Content-Type': 'application/json'
                },
                'body': json.dumps({
                    'message': 'Logout exitoso. Token invalidado.',
                    'method': 'token_sign_out'
                })
            }
        
        else:
            return {
                'statusCode': 400,
                'headers': {'Access-Control-Allow-Origin': '*'},
                'body': json.dumps({
                    'error': 'Se requiere "email" o "access_token" para hacer logout'
                })
            }
    
    except client.exceptions.NotAuthorizedException:
        return {
            'statusCode': 401,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': 'Token inválido o expirado'})
        }
    
    except client.exceptions.UserNotFoundException:
        return {
            'statusCode': 404,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': 'Usuario no encontrado'})
        }
    
    except json.JSONDecodeError:
        return {
            'statusCode': 400,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': 'Formato de JSON inválido'})
        }
    
    except KeyError as e:
        return {
            'statusCode': 400,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': f'Campo requerido faltante: {str(e)}'})
        }
    
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': f'Error interno del servidor: {str(e)}'})
        }
```
```json
{
  "body": "{\"email\": \"test@example.com\"}",
  "httpMethod": "POST"
}
```
```json
{
  "email": "test@example.com"
}
```

---

## **Api Gateway**:
### HTTP API - add Clouster - API server endpoint
- **API name**: micropay-api-gateway
  - **Integrations**:
    - Lambda
    - AWS Region: us-east-1
    - Method: GET
    - URL endpoint: arn:aws:lambda:us-east-1:123456789:function:micropay-lambda-register
  - **Integrations**:
    - Lambda
    - AWS Region: us-east-1
    - Method: GET
    - URL endpoint: arn:aws:lambda:us-east-1:123456789:function:micropay-lambda-login
  - **Integrations**:
    - Lambda
    - AWS Region: us-east-1
    - Method: GET
    - URL endpoint: arn:aws:lambda:us-east-1:123456789:function:micropay-lambda-logout    
- **Configure routes**:
  - User
    - **Method**: POST
    - **Resource path**: /auth/register
    - **Integration target**: micropay-lambda-register
- **Configure routes**:
  - User
    - **Method**: POST
    - **Resource path**: /auth/login
    - **Integration target**: micropay-lambda-login
- **Configure routes**:
  - User
    - **Method**: POST
    - **Resource path**: /auth/logout
    - **Integration target**: micropay-lambda-logout

---

## **ServiceDiscovery**: AWSCloudMap

---

## **CircuitBreaker**:

---
