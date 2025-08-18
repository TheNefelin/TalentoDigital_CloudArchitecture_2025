## **ECS**: Elastic Container Service

### ECS - Task definitions
- **Task definition family**: fin-tech-plus-task
- **AWS Fargate**: check
- **Amazon EC2 instances**: unchek
- **Operating system**: Linux/X86_64
- **CPU**: 1vCPU
- **Memory**: 2 GB
- **Task role**: LabRole
- **Task execution role**: LabRole
- **Name**: fin-tech-plus-app
- **Image URI**: ECR_IMAGE_URI
- **Essential container**: yes
- **Container port**: 3000
- **Protocol**: TCP
- **App protocol**: HTTP
- **Environment variables**:
  - PostgreSQL host
    - **Key**: DB_HOST
    - **Value type**: Value
    - **Value**: RDS_PGDB_URI
  - PostgreSQL port
    - **Key**: DB_PORT
    - **Value type**: Value
    - **Value**: 5432
  - PostgreSQL name
    - **Key**: DB_NAME
    - **Value type**: Value
    - **Value**: postgres
  - PostgreSQL user
    - **Key**: DB_USER
    - **Value type**: Value
    - **Value**: postgres
  - PostgreSQL password
    - **Key**: DB_PASSWORD
    - **Value type**: Value
    - **Value**: ****

### ECS - Clusters (Fargate + Docker)
- **Cluster name**: fin-tech-plus-cluster
- **AWS Fargate (serverless)**: check
- **Amazon EC2 instances**: uncheck
- **Create**:

### ECS - Clusters - Task
- Run new task:
  - **Task definition family**: fin-tech-plus-task
  - **Task definition revision**: last
  - **Desired tasks**: 1
  - **Capacity provider**: FARGATE
  - **Platform version**: LATEST
  - **VPC**: default
  - **Subnets**:
    - public-01
    - public-02
    - public-03
  - **Use an existing security group**: ecs-sg-fin-tech-plus
  - **Public IP** check

---
