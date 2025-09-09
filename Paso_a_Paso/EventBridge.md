## **Amazon EventBridge**: 
- **Create a new rule**: check
- **Rule name**: stop-ec2
- **Schedule expression**: check
- **Schedule expression**: rate(2 minute)

## **Lambda**: Relational Database Service
### Lambda SQS
- **Function name**: lambda-stop-ec2
- **Runtime**: Python 3.13
- **Architecture**: x86_64
- **Execution role**: LabRole
```py
import boto3
region = 'us-east-1'
instances = ['i-0680ba88f95e9a9c3']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
  ec2.stop_instances(InstanceIds=instances)
  print('stopped your instances: ' + str(instances))
```

## **Amazon EventBridge**: 
- **Create a new rule**: check
- **Rule name**: start-ec2
- **Schedule expression**: check
- **Schedule expression**: rate(2 minute)

## **Lambda**: Relational Database Service
### Lambda SQS
- **Function name**: lambda-start-ec2
- **Runtime**: Python 3.13
- **Architecture**: x86_64
- **Execution role**: LabRole
```py
import boto3
region = 'us-east-1'
instances = ['i-0680ba88f95e9a9c3']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
  ec2.start_instances(InstanceIds=instances)
  print('started your instances: ' + str(instances))
```

## **EC2**: Elastic Compute Cloud
###  Bastion
- **Name**: artema-ec2-bastion
- **OS Images**: Amazon Linux
- **Amazon Machine Image**: Amazon Linux 2023 kernel-6.1 AMI
- **Instance type**: t2.nano
- **Key pair**: vokey
- **VPC**: default
- **Subnet**: default
- **Auto-assign public IP**: enable
- **security groups**: artema-sg-bastion
- **Advanced details**:
  - **IAM instance profile**: LabInstanceProfile
  - **User data**
```bash
#!/bin/bash
yum update && yum upgrade -y
yum install -y httpd
systemctl enable httpd
systemctl start httpd
echo '<html><h1>EC2 Bastion Corriendo!!!</h1></html>' > /var/www/html/index.html
```
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