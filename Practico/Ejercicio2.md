# AWS - CLOUD COMPUTING EC2 EBS IP ELASTICA

<img src="..\Img\Ejercicio2.drawio.png">

---

## **VPC**: Virtual Private Cloud
### ejercicio2-vpc
- **VPC settings**: VPC and more
- **Name**: ejercicio2
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
### ejercicio2-sg-firewall
- **Name**: ejercicio2-sg-firewall
- **Description**: firewall
- **VPC**: ejercicio2-vpc
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
- **Outbound rules**:
  - Outbound
    - Type: All traffic
    - Protocol: all
    - Port range: all
    - Destination type: Custom
    - Destination: 0.0.0.0/0
    - Description: 

---

## **EC2**: 
### ejercicio1-lt-ec2-1
- **Name**: ejercicio2-ec2-1
- **OS Images**: Amazon Linux
- **Amazon Machine Image**: Amazon Linux 2023 kernel-6.1 AMI
- **Instance type**: t2.micro
- **Key pair**: vockey (.ppk)
- **VPC**: ejercicio2-vpc
- **Subnet**: ejercicio2-subnet-public1-us-east-1a
- **Auto-assign public IP**: Enable
- **security groups**: ejercicio2-sg-firewall
- **Advanced details**:
  - **User data**:
```bash
#!/bin/bash
yum install -y httpd
systemctl enable httpd
systemctl start httpd
echo '<html><h1>EC2 Corriendo!!!</h1></html>' > /var/www/html/index.html
```

### ejercicio2-lt-ec2-2
- **Name**: ejercicio2-ec2-2
- **OS Images**: Amazon Linux
- **Amazon Machine Image**: Amazon Linux 2023 kernel-6.1 AMI
- **Instance type**: t2.micro
- **Key pair**: vockey (.ppk)
- **VPC**: Ejercicio2-vpc
- **Subnet**: ejercicio2-subnet-public2-us-east-1b
- **Auto-assign public IP**: Enable
- **security groups**: ejercicio2-sg-firewall
- **Advanced details**:
  - **User data**:
```bash
#!/bin/bash
yum install -y httpd
systemctl enable httpd
systemctl start httpd
echo '<html><h1>EC2 Corriendo!!!</h1></html>' > /var/www/html/index.html
```

### ejercicio2-lt-ec2-3
- **Name**: ejercicio2-ec2-3
- **OS Images**: Windows
- **Amazon Machine Image**: Microsoft Windows Server 2025 Base
- **Instance type**: t3.medium
- **Key pair**: vockey (.ppk)
- **VPC**: ejercicio2-vpc
- **Subnet**: ejercicio2-subnet-public2-us-east-1b
- **Auto-assign public IP**: Enable
- **security groups**: ejercicio2-sg-firewall
- **Advanced details**:
  - **User data**:

---

## VPC: Elastic IPs
### Allocate Elastic IP address
-**Public IPv4 address pool**: 
-**Network border group**: us-east-1

### Associate Elastic IP address
- **Resource type**: Instance
- **Instance**: ejercicio2-ec2-1
- **Private IP address**: none

---