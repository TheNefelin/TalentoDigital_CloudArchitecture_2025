# App

```sh
npm install
```

```sh
node server.js
```

## **Seciruty Group**:
### artema-sg-rds
- **Name**: artema-sg-rds
- **Description**: Acceso MSSQL
- **VPC**: artema-vpc
- **Inbound rules**:
  - MSSQL
    - Type: MSSQL
    - Protocol: TCP
    - Port range: 1433
    - Destination type: Anywhere-IPv4
    - Destination: 0.0.0.0/0
    - Description: Acceso MSSQL
- **Outbound rules**:
  - Outbound
    - Type: All traffic
    - Protocol: all
    - Port range: all
    - Destination type: Custom
    - Destination: 0.0.0.0/0
    - Description:

### artema-sg-web
- **Name**: artema-sg-web
- **Description**: Acceso Web
- **VPC**: artema-vpc
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

## **RDS**:
### SQL Server Express
- **Database management type**: Amazon RDS
- **Edition**: SQL Server Express Edition
- **Templates**: Sandbox
- **DB instance identifier**: artema-rds-mssql
- **Master username**: admin
- **Credentials management**: Self managed
- **Master password**: ****
- **Burstable classes (includes t classes)**: db.t3.micro
- **Allocated storage**: 20
- **Virtual private cloud (VPC)**: artema-vpc
- **DB subnet group**: artema-subnet-public1-us-east-1a
- **Public access**: check
- **Existing VPC security groups**: artema-sg-rds

## **EC2**:
###  WebApp
- **Name**: artema-ec2-web
- **OS Images**: Amazon Linux
- **Amazon Machine Image**: Amazon Linux 2023 kernel-6.1 AMI
- **Instance type**: t2.nano
- **Key pair**: vockey
- **VPC**: artema-vpc
- **Subnet**: artema-subnet-public1-us-east-1a
- **Auto-assign public IP**: Enable
- **security groups**: artema-sg-web
- **Advanced details**:
  - **IAM instance profile**: LabInstanceProfile
- **SSH**
```sh
ssh -i "C:\Users\MyUser\Downloads\mi.pem" ec2-user@100.100.100.100 
```
```sh
sudo yum install -y nodejs npm 
```
- **Copiar proyecto** nueva ventana cmd
```sh
scp -i "ruta.pem" -r "ruta-app" ec2-user@100.100.100.100:/home/ec2-user/
```
```sh
cs MisActivos
```
```sh
npm install
```
```sh
sudo node server.js
```

---
