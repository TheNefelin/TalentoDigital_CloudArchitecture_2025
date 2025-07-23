# AWS Artema

## Diagrama

<img src=".\Img\Artema.drawio.png">

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
    - Destination: artema-sg-rds
    - Description: Acceso desde Bastion Host
- **Outbound rules**:
  - Outbound
    - Type: All traffic
    - Protocol: all
    - Port range: all
    - Destination type: Custom
    - Destination: 0.0.0.0/0
    - Description: 

### artema-sg-lambda
- **Name**: artema-sg-lambda
- **Description**:
- **VPC**: artema-vpc
- **Inbound rules**:
  - PostgreSQL (Desde Bastion)
    - Type: PostgreSQL
    - Protocol: 
    - Port range: 
    - Destination type: Custom
    - Destination:
    - Description:
- **Outbound rules**:
  - Outbound
    - Type: All traffic
    - Protocol: all
    - Port range: all
    - Destination type: Custom
    - Destination: 0.0.0.0/0
    - Description: 

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

## **Lambda**: (servicio funcional)
### artema-lambda-img

```python
import boto3
from datetime import datetime

def lambda_handler(event, context):
    s3 = boto3.client('s3', region_name='us-east-1')  # Cambia a tu región
    bucket_name = 'hell-s3'
    image_key = 'helldivers.jpg'
    
    try:
        # Verificación rápida (sin head_object para reducir tiempo)
        presigned_url = s3.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket_name, 'Key': image_key},
            ExpiresIn=3600
        )
        
        # return {
        #     'statusCode': 200,
        #     'body': presigned_url
        # }

        return {
            'statusCode': 302,
            'headers': {
                'Location': presigned_url
            }
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f"Error: {str(e)}"
        }
```

### artema-lambda-rds

```python
```

## **NAT Gateway**: Network Address Translation Gateway

## **API Gateway**: (servicio de enrutamiento)

## **CloudWatch**: (servicio de monitoreo)

