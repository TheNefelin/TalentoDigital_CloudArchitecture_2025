# AWS - VPC + EC2 + EFS (Elastic File System)

<img src="..\Img\Ejercicio3.drawio.png">

---

## **VPC**: Virtual Private Cloud
### ejercicio3-vpc
- **VPC settings**: VPC and more
- **Name**: ejercicio3
- **IPv4 CIDR block**: 10.0.0.0/16
- **Tenancy**: Default
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
- **Enable DNS hostnames**: check
- **Enable DNS resolution**: check

>**2 Private, 1 Table1, 1 NAT**

--- 

## **Seciruty Group**: 
### ejercicio3-sg-firewall
- **Name**: ejercicio3-sg-firewall
- **Description**: firewall
- **VPC**: ejercicio3-vpc
- **Inbound rules**:
  - SSH
    - Type: SSH
    - Protocol: TCP
    - Port range: 22
    - Destination type: Anywhere-IPv4
    - Destination: 0.0.0.0/0 (MyIP)
    - Description: Acceso remoto SSH 
  - Escritorio Remoto
    - Type: RDP
    - Protocol: TCP
    - Port range: 3389
    - Destination type: Anywhere-IPv4
    - Destination: 0.0.0.0/0 (MyIP)
    - Description: Acceso Escritorio Remoto
  - HTTP
    - Type: HTTP
    - Protocol: TCP
    - Port range: 80
    - Destination type: Anywhere-IPv4
    - Destination: 0.0.0.0/0
    - Description: Acceso web
  - Network File System
    - Type: NFS
    - Protocol: TCP
    - Port range: 80
    - Destination type: Anywhere-IPv4
    - Destination: 0.0.0.0/0
    - Description:  
- **Outbound rules**:
  - Outbound
    - Type: All traffic
    - Protocol: all
    - Port range: all
    - Destination type: Custom
    - Destination: 0.0.0.0/0
    - Description: 

---

## **EC2**: Elastic Compute Cloud
### Linux
- **Name**: ejercicio3-ec2-linux-efs
- **OS Images**: Amazon Linux
- **Amazon Machine Image**: Amazon Linux 2023 kernel-6.1 AMI
- **Instance type**: t2.micro
- **Key pair**: vockey (.ppk)
- **VPC**: ejercicio3-vpc
- **Subnet**: ejercicio3-subnet-public1-us-east-1a
- **Auto-assign public IP**: Enable
- **security groups**: ejercicio3-sg-firewall
- **Advanced details**:
  - **User data**:
```bash
#!/bin/bash
yum install -y httpd
systemctl enable httpd
systemctl start httpd
echo '<html><h1>EC2 Corriendo!!!</h1></html>' > /var/www/html/index.html
```
- **Number of instances**: 2

---

## **EFS**: Elastic File System
### ejercicio3-efs
- **Name**: ejercicio3-efs
- **VPC**: ejercicio3-vpc
- **Network**
  - **Manage**
    - **us-east-1a**:
      - **Security groups**: ejercicio3-sg-firewall
    - **us-east-1b**:
      - **Security groups**: ejercicio3-sg-firewall

### Attach
- **Mount via DNS**:
- **Using the EFS mount helper:**
```bash
sudo mount -t efs -o tls fs-0ef13b0195e7f8442:/ efs
```

## EC2-1 console and EC2-2 console
```bash
sudo su
yum install -y amazon-efs-utils
mkdir SHARED_FOLDER
ls
cd SHARED_FOLDER
pwd # ruta absoluta de la carpeta
cd
mount -t efs -o tls fs-0ef13b0195e7f8442:/ /home/ec2-user/SHARED_FOLDER
df -hT
ls /home/ec2-user/SHARED_FOLDER
echo "Datos Compartidos" | tee /home/ec2-user/SHARED_FOLDER/PruebaEFS.txt
ls /home/ec2-user/SHARED_FOLDER
cat /home/ec2-user/SHARED_FOLDER/PruebaEFS.txt
```

---

