
# 🧩 Caso resuelto — Representación de una Arquitectura Cloud Orientada a Microservicios (CloudServicesCo)

> **Contexto:** Modernización del monolito on‑premises hacia **AWS** con **microservicios** para mejorar escalabilidad, disponibilidad y velocidad de entrega.

---

## 1) Servicios clave seleccionados en AWS (mín. 5)

1. **Amazon API Gateway** — Entrada unificada para clientes web/mobile, validación de JWT, rate limiting.
2. **Amazon ECS (Fargate)** — Ejecución de contenedores sin administrar servidores (microservicios).
3. **Amazon RDS (Aurora MySQL)** — Transaccional para autenticación y pedidos.
4. **Amazon DynamoDB** — Catálogo de productos de lectura intensiva con latencias bajas.
5. **Amazon S3** — Almacenamiento de archivos estáticos (imágenes, reportes) y backups.
6. **Amazon CloudFront** — CDN para entregar contenido estático y media desde S3 con baja latencia.
7. **Amazon CloudWatch + AWS X-Ray** — Observabilidad (logs, métricas, trazas distribuidas).
8. **AWS Secrets Manager** — Gestión segura de secretos/credenciales.
9. **Elastic Load Balancer (ALB)** — Balanceo HTTP/HTTPS hacia tareas ECS dentro de VPC.
10. **Amazon VPC** — Segmentación de red (subnets públicas/privadas, Security Groups, NACLs).

> *Nota:* Kubernetes (EKS) también es válido; se elige **ECS Fargate** por simplicidad operativa en esta primera etapa.

---

## 2) Diagrama lógico de arquitectura (texto)

```
                   +---------------------------+
   Web/Mobile ---> |     Amazon API Gateway    | <--- Cognito (JWT opcional)
                   +-------------+-------------+
                                 |
                                 v
                         +-------+--------+
                         |   ALB (HTTP/S) |
                         +---+---------+--+
                             |         |
                 ------------+         +------------
                 |                               |
        +--------v-------+               +-------v--------+
        |  Auth Service  |               |  Orders Service|
        |  (ECS Fargate) |               | (ECS Fargate)  |
        +--------+-------+               +--------+-------+
                 |                               |
         +-------v-------+                +------v-------+
         |  RDS Aurora   |                |  RDS Aurora  |
         |  (MySQL)      |                |  (same cluster)
         +---------------+                +--------------+

                 +---------------------------------------+
                 |               Catalog Service         |
                 |              (ECS Fargate)           |
                 +--------------------+------------------+
                                      |
                               +------v------+
                               | DynamoDB    |
                               +-------------+

      +-----------------+                     +-------------------------+
      |      S3         |<-- assets/images -->|   CloudFront (CDN)      |
      +-----------------+                     +-------------------------+

  Observability: CloudWatch Logs/Metrics, X-Ray (tracing)
  Security: VPC (subnets privadas para ECS/RDS/DynamoDB), SG por capa, Secrets Manager
```

**Relaciones clave**
- API Gateway enruta por ruta/versión hacia ALB → tareas ECS (microservicios).
- **Auth** y **Orders** persisten en **RDS Aurora** (mismo clúster, esquemas separados).
- **Catalog** usa **DynamoDB** (lecturas rápidas, escalado automático).
- **S3 + CloudFront** sirven estáticos y media.
- Todo dentro de **VPC** con **Security Groups** y **subnets privadas** para backend.

---

## 3) Flujo de datos (end-to-end)

1. **Autenticación**
   - El cliente obtiene token (p. ej., **JWT** con Cognito o propio `Auth Service`).
   - API Gateway valida JWT (authorizer) y enruta al **Auth Service** cuando se requiera renovar/refrescar.

2. **Catálogo (lecturas intensivas)**
   - Cliente → API Gateway → **Catalog Service (ECS)**.
   - El servicio consulta **DynamoDB** (claves por `productId` y GSI por `category`).
   - Respuesta cacheable por el cliente/CDN cuando aplique.

3. **Pedidos (transaccional)**
   - Cliente → API Gateway → **Orders Service (ECS)** (con token válido).
   - **Orders** verifica stock consultando **Catalog** (read model en DynamoDB) o un **endpoint interno**.
   - Inserta/actualiza pedido en **RDS Aurora** usando transacciones.
   - Emite **eventos de dominio** (p. ej., `OrderPlaced`) para integraciones futuras (cola/SNS/SQS).

4. **Estáticos y media**
   - Imágenes y archivos servidos desde **CloudFront** (origen **S3**). Uploads controlados vía pre‑signed URLs.

5. **Observabilidad y seguridad**
   - Logs/métricas en **CloudWatch**, trazas distribuidas con **X‑Ray**.
   - Secretos (credenciales DB, API keys) en **Secrets Manager**.
   - **SG**: ALB (80/443 público), ECS privado (solo desde ALB/API Gateway), RDS (solo desde SG de ECS), DynamoDB (endpoint VPC).

---

## 4) Estimación básica de costos (opcional, aproximada)

> **Escenario de referencia (estimativo no contractual):**
> - 3 microservicios en **ECS Fargate**, cada uno con ~0.5 vCPU / 1 GB RAM, **2 réplicas** c/u (prod).
> - **API Gateway**: ~5 millones de requests/mes.
> - **RDS Aurora**: 1 clúster pequeño en una AZ (dev/test) o multi‑AZ (prod).
> - **DynamoDB**: on‑demand con tráfico moderado.
> - **S3 + CloudFront**: 200 GB almacenados, 1 TB de egress/mes.
>
> **Contribuciones típicas al costo mensual** (de mayor a menor, según uso):
> 1. **RDS Aurora** (capacidad y almacenamiento, + multi‑AZ).
> 2. **ECS Fargate** (vCPU/GB‑h según réplicas y horas activas).
> 3. **API Gateway** (por millón de requests).
> 4. **CloudFront/S3** (transferencia de datos y requests).
> 5. **DynamoDB** (lectura/escritura on‑demand) y **CloudWatch/X‑Ray**.
>
> **Sugerencias de optimización:**
> - Auto‑scaling por CPU/latencia/cola; apagar réplicas nocturnas en entornos no‑prod.
> - Caché agresiva de catálogo en CloudFront y cliente.
> - Elegir **Aurora Serverless v2** para cargas variables.
> - **Savings Plans/RI** para cargas estables.
> - Centralizar logs con retención ajustada y métricas pertinentes.

---

## 5) Reflexión breve

- **Prevención de cuellos de botella:** el diagrama evidencia puntos críticos (DB transaccional, picos en API Gateway, tamaño de tareas ECS), facilitando pruebas de carga dirigidas y planes de escalado.
- **Comunicación del equipo:** una vista común (diagrama + flujo) alinea a desarrollo, seguridad y operaciones; acelera decisiones y reduce malentendidos.
- **Anticipación de costos:** separar responsabilidades (RDS vs DynamoDB; compute ECS vs CDN) permite focalizar optimizaciones y proyecciones realistas antes del despliegue.

---

## 6) Anexos (checklist rápido)

- [ ] Rutas de API definidas y versionadas (`/v1/auth`, `/v1/catalog`, `/v1/orders`).
- [ ] Health checks y **readiness/liveness** en contenedores.
- [ ] Auto‑scaling (ECS service + target tracking).
- [ ] Backups/retención: RDS snapshots, versiones S3, export DynamoDB.
- [ ] IaC (CloudFormation/Terraform/CDK) para reproducibilidad.
- [ ] Monitoreo SLO/SLI (latencia p95, error rate, saturación).

---

# Desarrollo Paso a Paso

<img src="..\Img\M7\M7-Caso_01.png">
<img src="..\Img\M7\M7-Caso_02.png">

---

- ✔️ 3 repositorios en ECR
- ✔️ 1 base de datos en RDS PostgreSQL
- ✔️ 1 cluster en EKS
- ✔️ 1 node group con 2 nodos

---

## **Seciruty Group**:
### node-sg-service
- **Name**: node-sg-service
- **Description**: Access Node
- **VPC**: default
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
    - Destination type: Custom
    - Destination: postgres-sg-rds
    - Description: Acceso web
- **Outbound rules**:
  - Outbound
    - Type: All traffic
    - Protocol: all
    - Port range: all
    - Destination type: Custom
    - Destination: 0.0.0.0/0
    - Description:

### postgres-sg-rds
- **Name**: postgres-sg-rds
- **Description**: Acceso postgreSQL
- **VPC**: default
- **Inbound rules**:
  - PostgreSQL
    - Type: PostgreSQL
    - Protocol: TCP
    - Port range: 5432
    - Destination type: Custom
    - Destination: node-sg-service
    - Description: Acceso PostgreSQL
- **Outbound rules**:
  - Outbound
    - Type: All traffic
    - Protocol: all
    - Port range: all
    - Destination type: Custom
    - Destination: 0.0.0.0/0
    - Description:

## **RDS**: Relational Database Service
### PostgreSQL
- **Creation method**: Standard create
- **Engine type**: PostgreSQL
- **Templates**: Sandbox
- **Availability and durability**: Single-AZ DB instance deployment (1 instance)
- **DB instance**: pgdb-rds
- **Master username**: postgres
- **Credentials management**: ********
- **Instance configuration**:
    - Burstable classes (includes t classes)
    - db.t3.micro
- **Allocated storage**: 20 GiB
- **Enable storage autoscaling**: check
- **Compute resource**: Don’t connect to an EC2 compute resource
- **VPC**: default
- **DB subnet group**: default
- **Public access**: No
- **Security groups**: postgres-sg-rds
- **Monitoring**: Database Insights - Standard
- **Enhanced Monitoring**: Disabled  

```sql
-- auth-service
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- orders-service
CREATE TABLE IF NOT EXISTS orders (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    item VARCHAR(100),
    quantity INT
);

-- products-service
CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    price NUMERIC
);

INSERT INTO products 
    (name, price)
VALUES
    ('Laptop', 1200.50),
    ('Mouse', 25.99),
    ('Keyboard', 45.00),
    ('Monitor', 300.00),
    ('Headphones', 75.50);
```

## **ECR**: Elastic Container Registry
### Repositorio - auth-service-repo
- **Repository name**: auth-service-repo
- **Image tag mutability**: Mutable
- **Mutable tag exclusions**:
- **Encryption configuration**: AES-256
- **View push commands**

> [!CAUTION]
> View push commands from `auth-service-repo`.

### Repositorio - products-service-repo
- **Repository name**: products-service-repo
- **Image tag mutability**: Mutable
- **Mutable tag exclusions**:
- **Encryption configuration**: AES-256
- **View push commands**

> [!CAUTION]
> View push commands from `products-service-repo`.

### Repositorio - orders-service-repo
- **Repository name**: orders-service-repo
- **Image tag mutability**: Mutable
- **Mutable tag exclusions**:
- **Encryption configuration**: AES-256
- **View push commands**

> [!CAUTION]
> View push commands from `orders-service-repo`.

## **CloudShell**:
1. Modify aws-auth-service.yaml, aws-orders-service.yaml, aws-products-service.yaml and add <YOUR_ACCOUNT_ID> <YOUR-RDS-ENDPOINT> <YOUR-RDS-PASSWORD>
2. Open CloudShell
3. Run Commands
```sh
git clone https://github.com/TheNefelin/AWS_Microservices_Demo_NodeJS.git
cd AWS_Microservices_Demo_NodeJS
```
```sh
df -h
docker system prune -a --volumes -f
docker builder prune -f
df -h
```
```sh
git clone https://github.com/TheNefelin/AWS_Microservices_Demo_NodeJS.git
cd AWS_Microservices_Demo_NodeJS
```
```sh
aws ecr get-login-password --region ${REGION} | docker login --username AWS --password-stdin ${YOUR_ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com

docker build -f auth-service/Dockerfile -t auth-service-repo ./auth-service
docker tag auth-service-repo:latest ${YOUR_ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com/auth-service-repo:latest
docker push ${YOUR_ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com/auth-service-repo:latest

docker build -f orders-service/Dockerfile -t orders-service-repo ./orders-service
docker tag orders-service-repo:latest ${YOUR_ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com/orders-service-repo:latest
docker push ${YOUR_ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com/orders-service-repo:latest

docker build -f products-service/Dockerfile -t products-service-repo ./products-service
docker tag products-service-repo:latest ${YOUR_ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com/products-service-repo:latest
docker push ${YOUR_ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com/products-service-repo:latest

cd
```
```sh
docker images
rm -rf AWS_Microservices_Demo_NodeJS
docker system prune -a --volumes -f
docker builder prune -f
```

### Optional
1. Modify aws_cloudshel_docker.sh then add [YOUR_ACCOUNT_ID] and [REGION]
2. Modify aws-auth-service.yaml, aws-orders-service.yaml, aws-products-service.yaml and add <YOUR_ACCOUNT_ID> <YOUR-RDS-ENDPOINT> <YOUR-RDS-PASSWORD>
3. Upload aws_cloudshel_docker.sh aws-auth-service.yaml, aws-orders-service.yaml, aws-products-service.yaml files
4. Add execute permission to aws_cloudshel_docker.sh
```sh
chmod +x aws_cloudshel_docker.sh
```
5. Run aws_cloudshel_docker.sh
```sh
./aws_cloudshel_docker.sh
```

## **EKS**: Elastic Kubernetes Service
### Clusters
- **Configuration options**: Custom configuration
- **Use EKS Auto Mode**_ uncheck
- **Name**: node-microservices-demo
- **Cluster IAM role**: LabEksClusterRole
- **EKS API**: check
- **ARC Zonal shift**: disabled
- **VPC**: default
- **Subnets**: default
- **Additional security groups**: node-sg-service
- **Cluster endpoint access**: Public and private

### Clusters - Compute - Add node group
- **Name**: ng-general
- **Node IAM role**: LabRole
- **AMI type**: Amazon Linux 2023 (x86_64)
- **Instance types**: t3.medium
- **Disk size**: 20 GiB
- **Desired size**: 2
- **Minimum size**: 2
- **Maximum size**: 4
- **Subnets** default

### Clusters - Resources - Workload ???

## **CloudShell**:
### Create .yaml and upload
- auth-service.yaml
- orders-service.yaml
- products-service.yaml

### Update Kubernete Config (Connect kubectl to EKS)
```sh
aws eks update-kubeconfig --name node-microservices-demo --region <REGION>
``` 
```sh
kubectl get nodes
```
```sh
kubectl apply -f aws-auth-service.yaml
kubectl apply -f aws-orders-service.yaml
kubectl apply -f aws-products-service.yaml
```
```sh
kubectl get all
```
- optional
```sh
kubectl delete all --all
kubectl delete configmap --all
kubectl delete secret --all
```

## **Api Gateway**:
### HTTP API - add Clouster - API server endpoint
- **API name**: node-microservices-demo-api
  - **Integrations**:
    - HTTP
    - Method: GET
    - URL endpoint: https:// + auth-service-LoadBalancer-External-IP + :3000
  - **Integrations**:
    - HTTP
    - Method: POST
    - URL endpoint: https:// + auth-service-LoadBalancer-External-IP + :3000/api/register
  - **Integrations**:
    - HTTP
    - Method: POST
    - URL endpoint: https:// + auth-service-LoadBalancer-External-IP + :3000/api/login
  - **Integrations**:
    - HTTP
    - Method: GET
    - URL endpoint: https:// + orders-service-LoadBalancer-External-IP + :3000
  - **Integrations**:
    - HTTP
    - Method: ANY
    - URL endpoint: https:// + orders-service-LoadBalancer-External-IP + :3000/api/orders
  - **Integrations**:
    - HTTP
    - Method: GET
    - URL endpoint: https:// + products-service-LoadBalancer-External-IP + :3000
  - **Integrations**:
    - HTTP
    - Method: ANY
    - URL endpoint: https:// + products-service-LoadBalancer-External-IP + :3000/api/products
- **Configure routes**:
  - Auth
    - **Method**: GET
    - **Resource path**: /auth
    - **Integration target**: URL endpoint Auth
  - Auth
    - **Method**: POST
    - **Resource path**: /api/register
    - **Integration target**: URL endpoint Auth
  - Auth
    - **Method**: POST
    - **Resource path**: /api/login
    - **Integration target**: URL endpoint Auth
  - Orders
    - **Method**: GET
    - **Resource path**: /orders
    - **Integration target**: URL endpoint Orders
  - Orders
    - **Method**: ANY
    - **Resource path**: /api/orders
    - **Integration target**: URL endpoint Orders
  - Products
    - **Method**: GET
    - **Resource path**: /products
    - **Integration target**: URL endpoint Products
  - Products
    - **Method**: ANY
    - **Resource path**: /api/products
    - **Integration target**: URL endpoint Products

---