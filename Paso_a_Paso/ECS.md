## **ECS**: Elastic Container Service

### ECS - Clusters (Fargate + Docker)
- **Cluster name**: node-fargate-cluster
- **AWS Fargate (serverless)**: check
- **Amazon EC2 instances**: uncheck

### ECS - Task definitions
- **Task definition family**: Task definition family
- **AWS Fargate**: check
- **Amazon EC2 instances**: unchek
- **Operating system**: Linux/X86_64
- **CPU**: 1vCPU
- **Memory**: 2 GB
- **Task role**: LabRole
- **Task execution role**: LabRole
- **Name**: node-app
- **Image URI**: node:18-alpine
- **Essential container**: yes
- **Container port**: 3000
- **Protocol**: TCP
- **App protocol**: HTTP

---