# AWS - AUTOSCALING-LOADBALANCER

<img src="..\Img\Ejercicio1.drawio.png">

---

## **VPC**: Virtual Private Cloud
### ejercicio1-vpc
- **VPC settings**: VPC and more
- **Name**: ejercicio1
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
### artema-sg-bastion
- **Name**: ejercicio1-sg-firewall
- **Description**: firewall
- **VPC**: ejercicio1-vpc
- **Inbound rules**:
  - SSH
    - Type: SSH
    - Protocol: TCP
    - Port range: 22
    - Destination type: Anywhere-IPv4
    - Destination: 0.0.0.0/0 (MyIP)
    - Description: Acceso SSH temporal desde cualquier IP
  - Escritorio Remoto
    - Type: RDP
    - Protocol: TCP
    - Port range: 3389
    - Destination type: Anywhere-IPv4
    - Destination: 0.0.0.0/0 (MyIP)
    - Description: Acceso Escritorio Remoto desde cualquier IP
  - HTTP
    - Type: HTTP
    - Protocol: TCP
    - Port range: 80
    - Destination type: Anywhere-IPv4
    - Destination: 0.0.0.0/0
    - Description: Actualizaciones de paquetes
  - HTTPS
    - Type: HTTPS
    - Protocol: TCP
    - Port range: 443
    - Destination type: Anywhere-IPv4
    - Destination: 0.0.0.0/0
    - Description: Actualizaciones de paquetes
- **Outbound rules**:
  - Outbound
    - Type: All traffic
    - Protocol: all
    - Port range: all
    - Destination type: Custom
    - Destination: 0.0.0.0/0
    - Description: 

---

## **Launch Templates**:
### ejercicio1-lt-ec2
- **Name**: ejercicio1-lt-ec2
- **Description**: Plantilla base para instancias
- **OS Images**: Amazon Linux
- **Amazon Machine Image**: Amazon Linux 2023 kernel-6.1 AMI
- **Instance type**: t2.micro
- **Key pair**: artema-key (RSA) (.ppk)
- **Subnet**: ejercicio1-subnet-public1-us-east-1a
- **Availability Zone**: Don't include in launch template
- **security groups**: ejercicio1-sg-firewall
- **Advanced network configuration**:
  - **Auto-assign public IP**: Enable
- **Resource tags**
  - **Key**: Name
  - **Value**: ejercicio1-ec2-web
  - **Resource types**: Instances
- **Advanced details**:
  - **User data**
```bash
#!/bin/bash
yum install -y httpd
systemctl enable httpd
systemctl start httpd
echo '<html><h1>EC2 Corriendo!!!</h1></html>' > /var/www/html/index.html
```

---

## **Load balancers**:
### Target groups
- **target type**: Instances
- **Name**: ejercicio1-tg-ec2
- **Protocol**: HTTP
- **Port**: 80
- **VPC**: ejercicio1-vpc
- **Health check protocol**: HTTP 
- **Health check path**: /
- **Traffic port**: check
- **Healthy threshold**: 5
- **Unhealthy threshold**: 2
- **Timeout**: 5
- **Interval**: 30

### Load balancers
- **Name**: ejercicio1-lb-ec2
- **Scheme**: Internal
- **Load balancer IP address type**: IPv4
- **VPC**: ejercicio1-vpc
- **us-east-1a (use1-az4)**: ejercicio1-subnet-public1-us-east-1a
- **us-east-1b (use1-az6)**: ejercicio1-subnet-public2-us-east-1b
- **Security groups**: artema-sg-lb
- **Protocol**: HTTP
- **Port**: 80
- **Default action (target group)**: ejercicio1-tg-lb-ec2

---

## Auto Scaling
- **Name**: ejercicio1-asg
- **Launch template**: ejercicio1-lt-ec2
- **VPC**: ejercicio1-vpc
- **Availability Zones and subnets**:
  - ejercicio1-subnet-public1-us-east-1a 
  - ejercicio2-subnet-public2-us-east-1b
- **Availability Zone distribution**: Balanced best effort
- **Load balancing**: Attach to an existing load balancer
- **Attach to an existing load balancer**: Choose from your load balancer target groups
- **Existing load balancer target groups**: ejercicio1-tg-lb-ec2 | HTTP
- **Select VPC Lattice service to attach**: 
No VPC Lattice service
- **Health check**:
  - **Turn on Elastic Load Balancing health checks**: check
- **Health check grace period**: 60
- **Desired capacity** : 1
- **Min desired capacity**: 1
- **Max desired capacit**y: 4
- **Choose whether to use a target tracking policy**: Target tracking scaling policy
- **Scaling policy name**: ejercicio1-policy-ec2
- **Metric type**: Average CPU utilization
- **Target value**: 80
- **Instance warmup**: 60
- **Add notifications**: optional

---

## Stress
```bash
sudo yum install stress -y
stress --cpu 1 --timeout 400s
```