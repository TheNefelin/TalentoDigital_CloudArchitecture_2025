## **Auto Scaling**:
### Target groups
- **target type**: Instances
- **Name**: artema-tg-web
- **Protocol**: HTTP
- **Port**: 80
- **VPC**: artema-vpc
- **Health check protocol**: HTTP 
- **Health check path**: /
- **Traffic port**: check
- **Healthy threshold**: 5
- **Unhealthy threshold**: 2
- **Timeout**: 5
- **Interval**: 30

### Load balancers
- **Load balancer types**: Application Load Balancer
- **Name**: artema-lb-web
- **Scheme**: Internal
- **Load balancer IP address type**: IPv4
- **VPC**: artema-vpc
- **us-east-1a (use1-az4)**: artema-subnet-public1-us-east-1a
- **us-east-1b (use1-az6)**: artema-subnet-public2-us-east-1b
- **Security groups**: artema-sg-web
- **Protocol**: HTTP
- **Port**: 80
- **Default action (target group)**: artema-tg-web

### Auto Scaling
- **Name**: artema-asg
- **Launch template**: artema-lt-web
- **VPC**: artema-vpc
- **Availability Zones and subnets**:
  - artema-subnet-public1-us-east-1a 
  - artema-subnet-public2-us-east-1b
- **Availability Zone distribution**: Balanced best effort
- **Load balancing**: Attach to an existing load balancer
- **Attach to an existing load balancer**: Choose from your load balancer target groups
- **Existing load balancer target groups**: artema-tg-web | HTTP
- **Select VPC Lattice service to attach**: 
No VPC Lattice service
- **Health check**:
  - **Turn on Elastic Load Balancing health checks**: check
  - **Turn on Amazon EBS health checks**: check
- **Health check grace period**: 30
- **Desired capacity** : 1
- **Min desired capacity**: 1
- **Max desired capacit**y: 3
- **Choose whether to use a target tracking policy**: Target tracking scaling policy
- **Scaling policy name**: artema-policy-web
- **Metric type**: Average CPU utilization
- **Target value**: 50
- **Instance warmup**: 30
- **SNS Topic**: SNS Topic
- **Event types**:
  - **Launch**: check
  - **Terminate**: check
  - **Fail to launch**: check
  - **Fail to terminate**: check      

---
