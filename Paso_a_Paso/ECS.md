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

### App
- Estructura
```
FinTechPlusApi/
├── node_modules/
├── Dockerfile
├── package-lock.json
├── package.json
└── server.js
```

```sh
npm init -y
```

```sh
npm install express@4.18.2 cors uuid
```

- server.js
```javascript
const express = require('express');
const cors = require('cors');
const { v4: uuidv4 } = require('uuid');

const app = express();
const PORT = process.env.PORT || 3000;

// Middlewares
app.use(cors());
app.use(express.json());

// Base de datos en memoria (simulada)
let accounts = [
  {
    id: "1",
    name: "Juan Pérez",
    email: "juan@example.com",
    balance: 15000.50,
    currency: "USD",
    createdAt: new Date('2024-01-15')
  },
  {
    id: "2",
    name: "María García",
    email: "maria@example.com",
    balance: 8750.25,
    currency: "USD",
    createdAt: new Date('2024-02-01')
  }
];

// Ruta principal
app.get('/', (req, res) => {
  res.json({
    message: 'FinTechPlus API - Servicios Financieros',
    version: '1.0.0',
    endpoints: {
      accounts: '/api/accounts',
      health: '/health'
    }
  });
});

// Health check
app.get('/health', (req, res) => {
  res.json({
    status: 'OK',
    message: 'API funcionando correctamente',
    timestamp: new Date().toISOString(),
    uptime: process.uptime()
  });
});

// RUTAS DE CUENTAS

// GET /api/accounts - Obtener todas las cuentas
app.get('/api/accounts', (req, res) => {
  res.json({
    success: true,
    data: accounts,
    total: accounts.length
  });
});

// POST /api/accounts - Crear nueva cuenta
app.post('/api/accounts', (req, res) => {
  const { name, email, initialBalance = 0, currency = 'USD' } = req.body;
  
  if (!name || !email) {
    return res.status(400).json({
      success: false,
      message: 'Nombre y email son requeridos'
    });
  }
  
  const newAccount = {
    id: uuidv4(),
    name,
    email,
    balance: parseFloat(initialBalance),
    currency,
    createdAt: new Date()
  };
  
  accounts.push(newAccount);
  
  res.status(201).json({
    success: true,
    message: 'Cuenta creada exitosamente',
    data: newAccount
  });
});

// Middleware para rutas no encontradas
app.use('*', (req, res) => {
  res.status(404).json({
    success: false,
    message: 'Endpoint no encontrado',
    availableEndpoints: [
      'GET /',
      'GET /health',
      'GET /api/accounts',
      'POST /api/accounts'
    ]
  });
});

// Middleware de manejo de errores
app.use((error, req, res, next) => {
  console.error('Error:', error);
  res.status(500).json({
    success: false,
    message: 'Error interno del servidor'
  });
});

// Iniciar servidor
app.listen(PORT, '0.0.0.0', () => {
  console.log(`🚀 FinTechPlus API ejecutándose en puerto ${PORT}`);
  console.log(`📊 Health check: http://localhost:${PORT}/health`);
  console.log(`💰 Cuentas: ${accounts.length}`);
});

module.exports = app;
```

Dockerfile
```dockerfile
# Usar imagen base oficial de Node.js (versión LTS Alpine)
FROM node:18-alpine

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /usr/src/app

# Copiar archivos de dependencias primero (para aprovechar cache de Docker)
COPY package*.json ./

# Instalar dependencias
RUN npm ci --only=production && npm cache clean --force

# Crear usuario no privilegiado para mayor seguridad
RUN addgroup -g 1001 -S nodejs && adduser -S fintech -u 1001

# Copiar el código fuente de la aplicación
COPY --chown=fintech:nodejs . .

# Cambiar al usuario no privilegiado
USER fintech

# Exponer el puerto en el que la API escucha
EXPOSE 3000

# Comando para ejecutar la aplicación
CMD ["node", "server.js"]
```

- Comprimir Projecto
```sh
FinTechPlusApi.zip
```

---

## **4. CloudShell**:

- Subir el archivo comprimido `FinTechPlusApi.zip`
```sh
ls
ls -a
```
```sh
unzip FinTechPlusApi.zip
```
```sh
cd FinTechPlusApi
```

- Utilizar los comandos `View push commands` de `fin-tech-plus-repo` para crear la imagen docker en el repositorio.
```sh
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 123.dkr.ecr.us-east-1.amazonaws.com
```
```sh
docker build -t fin-tech-plus-repo .
```
```sh
docker tag fin-tech-plus-repo:latest 123.dkr.ecr.us-east-1.amazonaws.com/fin-tech-plus-repo:latest
```
```sh
docker push 123.dkr.ecr.us-east-1.amazonaws.com/fin-tech-plus-repo:latest
```

- Después del build, probar localmente
```sh
docker run -d -p 3000:3000 --name fintech-test fin-tech-plus-repo
curl http://localhost:3000/health
```
- Verificar que la imagen se subió correctamente:
```sh
aws ecr describe-images --repository-name fin-tech-plus-repo
```
-
```sh
docker ps
docker stop [CONTAINER_ID]
```

### Limpiar CloudShell
- Listas de imagenes
```sh
docker images
```
- Eliminar imagen específica
```sh
docker rmi -f [IMAGE_ID]
```
- Limpieza completa de Docker
```sh
docker images
df -h
```
```sh
docker system prune -af
docker volume prune -f
```
```sh
rm -f FinTechPlusApi.zip
rm -rf FinTechPlusApi/
```

---
