# **EC2 Auto Scaling:**

### 5.1 Launch template
- **Name**: artema-lt-ec2
- **Description**: Plantilla base para instancias
- **OS Images**: Amazon Linux
- **Amazon Machine Image**: Amazon Linux 2023 kernel-6.1 AMI
- **Instance type**: t3.micro
- **Key pair**: vockey (.ppk)
- **Subnet**: Don't include in launch template
- **Availability Zone**: Don't include in launch template
- **security groups**: artema-sg-firewall
- **Advanced network configuration**:
  - **Auto-assign public IP**: Enable
- **Resource tags**
  - **Key**: Name
  - **Value**: artema-ec2-web
  - **Resource types**: Instances
- **Advanced details**:
  - **IAM instance profile**: LabInstanceProfile
  - **User data**
```bash
#!/bin/bash
yum update -y
yum install nginx -y
yum install awscli -y
aws s3 sync s3://mediastream-s3-storage/ /usr/share/nginx/html/
chown -R nginx:nginx /usr/share/nginx/html/
chmod -R 755 /usr/share/nginx/html/
systemctl stop httpd
systemctl disable httpd
systemctl enable nginx
systemctl start nginx
```

### 5.2 Target Groups
- **target type**: Instances
- **Name**: mediastream-tg-ec2
- **Protocol**: HTTP
- **Port**: 80
- **VPC**: mediastream-vpc
- **Health check protocol**: HTTP 
- **Health check path**: /
- **Advanced health check settings**:
  - **Traffic port**: check
  - **Healthy threshold**: 5
  - **Unhealthy threshold**: 2
  - **Timeout**: 5
  - **Interval**: 30

### 5.3 Load Balancers
- **Load balancer types**: Application Load Balancer
- **Name**: mediastream-lb-ec2
- **Scheme**: Internal
- **Load balancer IP address type**: IPv4
- **VPC**: mediastream-vpc
- **us-east-1a (use1-az4)**: mediastream-subnet-public1-us-east-1a
- **us-east-1b (use1-az6)**: mediastream-subnet-public2-us-east-1b
- **Security groups**: mediastream-sg-lb
- **Protocol**: HTTP
- **Port**: 80
- **Default action (target group)**: mediastream-tg-ec2

### 5.4 Auto Scaling Groups
- **Name**: mediastream-asg
- **Launch template**: mediastream-lt-ec2
- **VPC**: mediastream-vpc
- **Availability Zones and subnets**:
  - mediastream-subnet-public1-us-east-1a 
  - mediastream-subnet-public2-us-east-1b
- **Availability Zone distribution**: Balanced best effort
- **Load balancing**: Attach to an existing load balancer
- **Attach to an existing load balancer**: Choose from your load balancer target groups
- **Existing load balancer target groups**: mediastream-tg-ec2 | HTTP
- **Select VPC Lattice service to attach**: 
No VPC Lattice service
- **Health check**:
  - **Turn on Elastic Load Balancing health checks**: check
- **Health check grace period**: 30
- **Desired capacity** : 1
- **Min desired capacity**: 1
- **Max desired capacit**y: 4
- **Choose whether to use a target tracking policy**: Target tracking scaling policy
- **Scaling policy name**: mediastream-policy-ec2
- **Metric type**: Average CPU utilization
- **Target value**: 80
- **Instance warmup**: 30
- **Disable scale in to create only a scale-out policy** uncheck
- **Additional settings**:
  - **Enable group metrics collection within CloudWatch**: check
- **Add notifications**: mediastream-sns

---
