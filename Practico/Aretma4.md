# AWS Artema Aplicación .NET 8 + PostgreSQL + Angular 20
- EB (Elastic Beanstalk)
- RDS (Relational Database Service)

## Diagrama

<img src="..\Img\Artema1.drawio.png">


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
