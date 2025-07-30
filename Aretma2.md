# AWS Artema

## Diagrama

<img src=".\Img\Artema.drawio.png">

## **VPC**: Virtual Private Cloud
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
- **NAT gateways**: 1 per AZ
- **VPC endpoints**: None
- **Enable DNS hostnames**: check
- **Enable DNS resolution**: check

---

## **Seciruty Group**: 
### artema-sg-bastion
- **Name**: artema-sg-bastion
- **Description**: SG para Bastion Host (acceso SSH + conexion a RDS)
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
    - Description: Conexion a RDS PostgreSQL  
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
    - Description: Acceso desde Bastion a PostgreSQL   
- **Outbound rules**:
  - Outbound
    - Type: All traffic
    - Protocol: all
    - Port range: all
    - Destination type: Custom
    - Destination: 0.0.0.0/0
    - Description: 

### artema-sg-lb
- **Name**: artema-sg-lb
- **Description**: SG para Load balancers
- **VPC**: artema-vpc
- **Outbound rules**:
  - Outbound
    - Type: All traffic
    - Protocol: all
    - Port range: all
    - Destination type: Custom
    - Destination: 0.0.0.0/0
    - Description: 

---

## **EC2 Launch Template**:
### artema-lt-ec2-bastion
- **Name**: artema-lt-ec2-bastion
- **Description**: Micro EC2 Bastion
- **Template tags**
  - Add new tag
    - **Key**: Name
    - **Value**: artema-ec2-bastion
- **OS Images**: Amazon Linux
- **Amazon Machine Image**: Amazon Linux 2023 kernel-6.1 AMI
- **Instance type**: t2.nano
- **Key pair**: artema-key (RSA) (.ppk)
- **Subnet**: Don't include in launch template
- **Availability Zone**: Don't include in launch template
- **security groups**: artema-sg-bastion
- **Advanced network configuration**:
  - **Auto-assign public IP**: Enable

### Launch instance from template
- **Source template**: artema-lt-ec2-bastion
- **Availability Zone**: us-east-1a or us-east-1b
- **Subnet**: artema-subnet-public1-us-east-1a or artema-subnet-public2-us-east-1b

---

## **EC2 Load balancers**:
### Target groups
- **Group Details**: Application Load Balancer
- **Name**: artema-target-lb
- **VPC**: artema-vpc
- **Application Load Balancer**: artema-lb-bastion

### Load balancers
- **Name**: artema-lb-bastion
- **VPC**: artema-vpc
- **us-east-1a (use1-az4)**: artema-subnet-public1-us-east-1a
- **us-east-1b (use1-az6)**: artema-subnet-public2-us-east-1b
- **Security groups**: artema-sg-lb


### artema-lb-rds
- **Name**: artema-lb-rds
- **VPC**: artema-vpc
- **us-east-1a (use1-az4)**: artema-subnet-public1-us-east-1a
- **us-east-1b (use1-az6)**: artema-subnet-public2-us-east-1b
- ****

---

## **EC2**: Elastic Compute Cloud (servicio de servidores virtuales)
### artema-ec2-bastion
- **Name**: artema-ec2-bastion
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
- **Password: ****

---

## **RDS**:

---

## **RDS**: Relational Database Service 
### DB Subnet Group
- **Name**: artema-sng-rds
- **Description**: Subnet group para RDS PostgreSQL en subredes privadas
- **VPC**: artema-vpc
- **Availability Zones**:
    - us-east-1a
    - us-east-1b
- **Subnets**:
    - artema-subnet-private1-us-east-1a
    - artema-subnet-private2-us-east-1b

### DB PostgreSQL
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
- **Connectivity**: Don’t connect to an EC2 compute resource
- **VPC**: artema-vpc
- **DB subnet group**: artema-sng-rds
- **Public access**: No
- **Security groups**: artema-sg-rds
- **Enhanced Monitoring**: Disabled

---
