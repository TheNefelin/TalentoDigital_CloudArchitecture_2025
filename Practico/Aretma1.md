# AWS Artema

## Diagrama

<img src="..\Img\Artema1.drawio.png">

## **VPC**: Virtual Private Cloud
### Configuracion
- VPC settings: VPC and more
- Name: artema
- IPv4 CIDR block: 10.0.0.0/16
- IPv6 CIDR block: No IPv6 CIDR block
- Number of Availability Zones: 2
- Customize AZs:
  - us-east-1a
  - us-east-1b
- Number of public subnets: 2
- Number of private subnets: 2
- Customize subnets CIDR blocks:
  - Public subnet CIDR block in us-east-1a: 10.0.0.0/20
  - Public subnet CIDR block in us-east-1b: 10.0.16.0/20
  - Private subnet CIDR block in us-east-1a: 10.0.128.0/20
  - Private subnet CIDR block in us-east-1b: 10.0.144.0/20
- NAT gateways: In 1 AZ
- VPC endpoints: None
- Enable DNS hostnames: check
- Enable DNS resolution check

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

## **Seciruty Group**: (reglas de seguridad)
### artema-sg-bastion
- **Name**: artema-sg-bastion
- **Description**: SG para Bastion Host (acceso SSH + conexión a RDS)
- **VPC**: artema-vpc
- **Inbound rules**:
  - SSH
    - Type: SSH
    - Protocol: TCP
    - Port range: 22
    - Destination type: Anywhere-IPv4
    - Destination: 0.0.0.0/0 (MyIP)
    - Description: Acceso SSH temporal desde cualquier IP
  - HTTPS
    - Type: HTTPS
    - Protocol: TCP
    - Port range: 443
    - Destination type: Anywhere-IPv4
    - Destination: 0.0.0.0/0
    - Description: Actualizaciones de paquetes
  - PostgreSQL (Hacia RDS)
    - Type: PostgreSQL
    - Protocol: TCP
    - Port range: 5432
    - Destination type: Custom
    - Destination: artema-sg-rds
    - Description: Conexión a RDS PostgreSQL  
- **Outbound rules**:
  - Outbound
    - Type: All traffic
    - Protocol: all
    - Port range: all
    - Destination type: Custom
    - Destination: 0.0.0.0/0
    - Description: 

### artema-sg-rds
- **Name**: artema-sg-rds
- **Description**: SG para RDS PostgreSQL (solo acceso desde Bastion)
- **VPC**: artema-vpc
- **Inbound rules**:
  - PostgreSQL (Desde Bastion)
    - Type: PostgreSQL
    - Protocol: TCP
    - Port range: 5432
    - Destination type: Custom
    - Destination: artema-sg-bastion
    - Description: Acceso desde Bastion Host
  - PostgreSQL (Desde Lambda)
    - Type: PostgreSQL
    - Protocol: TCP
    - Port range: 5432
    - Destination type: Custom
    - Destination: artema-sg-lambda-rds
    - Description: Acceso desde Lambda    
- **Outbound rules**:
  - Outbound
    - Type: All traffic
    - Protocol: all
    - Port range: all
    - Destination type: Custom
    - Destination: 0.0.0.0/0
    - Description: 

### artema-sg-lambda-img
- **Name**: artema-sg-lambda-img
- **Description**: Permite trafico de salida desde Lambda hacia S3
- **VPC**: artema-vpc
- **Outbound rules**: (Hacia S3)
  - Outbound
    - Type: HTTPS
    - Protocol: TCP
    - Port range: 443
    - Destination type: Custom
    - Destination: pl-63a5400a
    - Description: Permite trafico seguro a S3 desde Lambda

### artema-sg-lambda-rds
- **Name**: artema-sg-lambda-rds
- **Description**: Permite trafico de salida desde Lambda hacia RDS
- **VPC**: artema-vpc
- **Outbound rules**:
  - Outbound
    - Type: PostgreSQL
    - Protocol: TCP
    - Port range: 5432
    - Destination type: Custom
    - Destination: artema-sg-rds
    - Description: Permite trafico seguro a RDS desde Lambda    

## **EC2**: Elastic Compute Cloud (servicio de servidores virtuales)
- **Name**: artema-bastion
- **OS Images**: Amazon Linux
- **Amazon Machine Image**: Amazon Linux 2023 kernel-6.1 AMI
- **Instance type**: t2.micro
- **Key pair**: artema-key (RSA) (.ppk)
- **VPC**: artema-vpc
- **Subnet**: artema-subnet-public1-us-east-1a
- **Auto-assign public IP**: Enable
- **security groups**: artema-sg-bastion
- **Allow SSH traffic from**: 0.0.0.0/0 (MyIP)

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

### pgAdmin
- **Name**: AWS-artema
- **Host**: RDS-Endpoint
- **Port**: 5433
- **Database**: postgres
- **Username**: postgres
- **Password: ******

## **S3**: Simple Storage Service, Bucket (servicio de almacenamiento)
### backet artema-s3-rds
- **AWS Region**: us-east-1
- **Name**: artema-s3-rds
- **Object Ownership**: ACLs disabled
- **Block all public access**: check
- **Bucket Versioning**: Enable
- **Encryption type**: SSE-S3
- **Bucket Key**: Disable
- **Management**
    - Create lifecycle rule: 
        - Name: artema-rds-glacier-backup
        - Choose a rule scope: Apply to all objects in the bucket
        - Lifecycle rule actions: Permanently delete...
        - Days after objects become noncurrent: 7
        - Number of newer versions to retain: 2

### backet artema-s3-storage
- **AWS Region**: us-east-1
- **Name**: artema-s3-storage
- **Object Ownership**: ACLs disabled
- **Block all public access**: check
- **Bucket Versioning**: Disable
- **Encryption type**: SSE-S3
- **Bucket Key**: Disable

```
S3
└── Bucket: mi-sitio-estatico
    ├── index.html
    ├── logo.png
    └── css/
        └── estilos.css
```

## **RDS**: Relational Database Service (servicio de base de datos)
### DB Subnet Group
- **Name**: artema-rds-sng
- **Description**: Subnet group para RDS PostgreSQL en subredes privadas
- **VPC**: artema-vpc
- **Availability Zones**:
    - us-east-1a
    - us-east-1b
- **Subnets**:
    - artema-subnet-private1-us-east-1a
    - artema-subnet-private2-us-east-1b

```sql
CREATE TABLE personajes_hxh (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    tipo_nen VARCHAR(50) NOT NULL,
    edad INT NOT NULL,
    descripcion TEXT,
    img VARCHAR(100)
);
```

```sql
INSERT INTO personajes_hxh 
    (nombre, tipo_nen, edad, descripcion, img)
VALUES
    ('Gon Freecss', 'Enhancer', 12, 'Protagonista, con gran talento natural para el Nen.', 'gon.webp'),
    ('Killua Zoldyck', 'Transmuter', 12, 'Hijo de la familia asesina Zoldyck, amigo cercano de Gon.', 'killua.webp'),
    ('Kurapika', 'Conjurer', 17, 'Último sobreviviente del clan Kurta, busca venganza.', 'kurapika.webp'),
    ('Leorio Paradinight', 'Emitter', 19, 'Aspira a ser médico, es valiente y decidido.', 'leorio.webp'),
    ('Hisoka Morow', 'Transmuter', 28, 'Antagonista impredecible, disfruta de la pelea.', 'hisoka.webp'),
    ('Chrollo Lucilfer', 'Specialist', 30, 'Líder de la banda de ladrones Fantasma.', 'chrollo.webp'),
    ('Biscuit Krueger', 'Enhancer', 30, 'Maestra experimentada con apariencia joven.', 'biscuit.webp');
```

```sql
SELECT * FROM personajes_hxh;
```

```sql
DROP TABLE IF EXISTS personajes_hxh;
```

### DataBase
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
- **Allocated storage**: 3GiB
- **Connectivity**: Connect to an EC2 compute resource
- **Compute resource**: artema-bastion
- **VPC**: artema-vpc
- **DB subnet group**: artema-rds-sng
- **Public access**: No
- **Security groups**: artema-sg-rds
- **Enhanced Monitoring**: Disabled

### Snapshots
- **Snapshot type**: DB instance
- **DB instance**: artema-pgdb
- **Snapshot name**: artema-manual-snapshot-20250723
- **Actions**
    - Export to Amazon S3
- **Export identifier**: artema-export-pgdb-20250723
- **Amount of data to be exported**: All (20 GB)
- **S3 bucket**: artema-s3-rds
- **IAM role**: LabRole

## **Lambda**: (servicio funcional)
### artema-lambda-img
- **Function name**: artema-lambda-img
- **Runtime**: Python 3.13
- **Architecture**: x86_64
- **Execution role**: LabRole
- **VPC**: artema-vpc
- **Subnets**
    - artema-subnet-private2-us-east-1a
    - artema-subnet-private2-us-east-1b
- **Security groups**: artema-sg-lambda-img

### Environment variable
- **S3_BUCKET_NAME**: artema-s3-storage

```python
import boto3
import os

def lambda_handler(event, context):
    bucket_name = os.environ['S3_BUCKET_NAME']
    
    image_name = event.get('pathParameters', {}).get('image-name')

    if not image_name:
        return {
            'statusCode': 400,
            'body': "Error: Falta el parámetro 'image' en el query string."
        }
    
    if not image_name.lower().endswith('.webp'):
        return {
            'statusCode': 400,
            'body': "Error: Solo se permiten archivos con extensión .webp."
        }
    
    image_key = f"img/{image_name}"
    s3 = boto3.client('s3', region_name='us-east-1')
    
    try:
        s3.head_object(Bucket=bucket_name, Key=image_key)
        
        presigned_url = s3.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket_name, 'Key': image_key},
            ExpiresIn=3600  # 1 hora de validez
        )
        
        return {
            'statusCode': 302,
            'headers': {
                'Location': presigned_url
            }
        }
    
    except s3.exceptions.ClientError as e:
        if e.response['Error']['Code'] == '404':
            return {
                'statusCode': 404,
                'body': f"Error: El archivo '{image_name}' no existe en el bucket."
            }
        else:
            return {
                'statusCode': 500,
                'body': f"Error interno: {str(e)}"
            }
```

```json
{
  "pathParameters": {
    "image-name": "hisoka.webp"
  }
}
```

### artema-lambda-rds
- **Function name**: artema-lambda-rds
- **Runtime**: Python 3.13
- **Architecture**: x86_64
- **Execution role**: LabRole
- **VPC**: artema-vpc
- **Subnets**
    - artema-subnet-private2-us-east-1a
    - artema-subnet-private2-us-east-1b
- **Security groups**: artema-sg-lambda-rds

### Environment variable
- **DB_HOST**: rds-host
- **DB_PORT**: 5432
- **DB_NAME**: postgres
- **DB_USER**: postgres
- **DB_PASS**: *****
- **URI**: https://6ga2qyue32.execute-api.us-east-1.amazonaws.com/img/

### psycopg2-binary
- Es una versión empaquetada de psycopg2 (con los binarios incluidos) que facilita su instalación sin compilar.

1. crear projecto puthon vscode
```
lambda-psycopg2-layer/
```
2. instalar pg8000
```bash
pip install pg8000 -t python
```
```
lambda-psycopg2-layer/
  └── python
```
3. comprimir la carpeta python
```
- python -> python.zip
```
4. subir python.zip a layer para lambda (py-pg8000-layer)
    - **Name**: py-pg8000-layer
    - **Description**: Capa para conexión a PostgreSQL desde Lambda usando pg8000 
    - **Upload a .zip file**: python.zip
    - **Compatible architectures**: x86_64
    - **Compatible runtimes**: Python 3.13
5. agregar layer a lambda (py-pg8000-layer)
    - **Custom layers**: py-pg8000-layer
    - **Version**: 1

```python
import os
import json
import pg8000.native
from decimal import Decimal

def lambda_handler(event, context):
    DB_HOST = os.environ['DB_HOST']
    DB_PORT = os.environ['DB_PORT']
    DB_NAME = os.environ['DB_NAME']
    DB_USER = os.environ['DB_USER']
    DB_PASS = os.environ['DB_PASS']

    try:
        conn = pg8000.native.Connection(
            host=DB_HOST,
            port=DB_PORT,         
            database=DB_NAME,   
            user=DB_USER,
            password=DB_PASS,            
        )
        
        rows = conn.run("SELECT * FROM personajes_hxh")
        columns = [desc["name"] for desc in conn.columns]
        result = [dict(zip(columns, row)) for row in rows]
        
        conn.close()

        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps(result, default=decimal_handler)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

def decimal_handler(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError
```

## **API Gateway**: (servicio de enrutamiento)
### API for artema-lambda-img
- **API type**: HTTP API
- **Name**: artema-api-gw-img
- **Routes**
    - Route and method: GET
    - Route name: /img/{image-name}
- **Integration**: Attach integration
- **Integration details**: Create and attach an integration
- **Integration type**: Lambda function
- **AWS Region**: us-east-1
- **Lambda function**: artema-lambda-img
- **Stages**
    - $default : https://6ga2qyue32.execute-api.us-east-1.amazonaws.com/img/{image-name}

### API for artema-lambda-rds
- **API type**: HTTP API
- **Name**: artema-api-gw-rds
- **Routes**
    - Route and method: GET
    - Route name: /hunters
- **Integration**: Attach integration
- **Integration details**: Create and attach an integration
- **Integration type**: Lambda function
- **AWS Region**: us-east-1
- **Lambda function**: artema-lambda-rds
- **Stages**
    - $default : https://2g2796no0c.execute-api.us-east-1.amazonaws.com/hunters
- **CORS**
    - Access-Control-Allow-Origin: *
    - Access-Control-Allow-Headers: content-type
    - Access-Control-Allow-Methods: GET
    - Access-Control-Allow-Credentials: NO
    
## **CloudWatch**: (servicio de monitoreo)

## **NAT Gateway**: Network Address Translation Gateway

