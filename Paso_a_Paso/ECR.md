## **ECR**: Elastic Container Registry
### Repositorio desde local
- **Repository name**: node-app-repo
- **Image tag mutability**: Mutable
- **Mutable tag exclusions**:
- **Encryption configuration**: AES-256
---

### Repositorio Node con archivos local

```mermaid
flowchart TD
  A[Crear Dockerfile + index.js, package.json] --> B[Construir imagen Docker]
  B --> C[Subir imagen a ECR (docker push)]
  C --> D[Crear Task Definition en ECS con imagen y configuración CPU, memoria, puertos]
  D --> E[Configurar VPC y Subnets públicas]
  E --> F[Configurar Security Group, puerto 3000 abierto]
  F --> G[Ejecutar Task en ECS Fargate - Run Task]
  G --> H[Obtener IP pública de la tarea]
  H --> I[Acceder a la app vía navegador en IP:3000]
```

- Iniciar Sesion en AWS CLI o CloudShell web de AWS
```bash
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 123456.dkr.ecr.us-east-1.amazonaws.com
```

- index.js
```javascript
const http = require('http');
const PORT = process.env.PORT || 3000;

const server = http.createServer((req, res) => {
  res.end('¡Hola desde Node.js en AWS App Runner!');
});

server.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

- package.json
```json
{
  "name": "aws-apprunner-node",
  "version": "1.0.0",
  "main": "index.js",
  "scripts": {
    "start": "node index.js"
  },
  "dependencies": {}
}
```

- Dockerfile
```
FROM node:18-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

CMD ["npm", "start"]
```

- Crea la imagen Docker
```bash
docker build -t node-app-repo .
```

- Etiqueta la imagen para ECR
```bash
docker tag node-app-repo:latest 123456.dkr.ecr.us-east-1.amazonaws.com/node-app-repo:latest
```

- Sube la imagen a ECR
```bash
docker push 123456.dkr.ecr.us-east-1.amazonaws.com/node-app-repo:latest
```

- Lista las imagens
```bash
docker images
```

- Corre la imagen
```bash
docker run -p 3000:3000 node-app-repo
```

```bash
docker rmi bb7229c9e939
docker rmi -f bb7229c9e939
```

### ECS: Clusters con Fargate
- **Cluster name**: Cluster name
- **AWS Fargate (serverless)**: check
- **Amazon EC2 instances**: uncheck
- **Task role**: LabRole
- **Task execution role**: LabRole
- **Container details**:
  - **Name**: node-app-repo
  - **Image URI**: 
  - **Essential container**: Yes
- **Container port** 3000

### ECS: Task definitions
- **Task definition family**: node-app-task
- **AWS Fargate**: check

**Deploy**: Run Task
- **Capacity provider**: FARGATE
- **VPC**: my-vpc
- **Subnets**:
  - Public1
  - Public2
  - Public3    
- **Security group name**: Default

### AWS App Runner (SIN PERMISO)
- **Repository type**: Container registry
- **Provider**: Amazon ECR
- **Container image URI**: 123456.dkr.ecr.us-east-1.amazonaws.com/node-app-repo
- **Deployment trigger**: Manual
- **Create new service role**: AppRunnerECRAccessRole
- **Service name**: node-app
- **Port**: 3000

---

### Repositorio Node con Docker
- Iniciar Sesion en AWS CLI o CloudShell web de AWS
```bash
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 123456789012.dkr.ecr.us-east-1.amazonaws.com
```

