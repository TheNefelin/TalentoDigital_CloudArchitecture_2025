# 💪 Análisis de Caso: Implementación mediante Contenedores de Aplicación

## 📍 Situación Inicial

La empresa **FinTechPlus**, dedicada a servicios financieros, ejecuta
actualmente su aplicación **monolítica en servidores locales**.
Los principales problemas detectados son:
- Inconsistencias entre entornos de desarrollo, prueba y producción.
- Dificultades de mantenimiento y escalabilidad.
- Dependencias conflictivas de Node.js y paquetes npm entre diferentes entornos.

Para resolverlo, se decide **migrar la aplicación a contenedores con
Docker**, logrando:
- Homogeneidad en los entornos.
- Despliegues más rápidos.
- Mayor flexibilidad operativa.
- Aislamiento de dependencias..

---

## 🔎 Descripción del Caso

Como ingeniero DevOps encargado del proceso, las responsabilidades
incluyen:
1. Analizar los desafíos actuales.
2. Diseñar y crear un **Dockerfile** con todas las dependencias.
3. Configurar **volúmenes y redes**.
4. Documentar ventajas, limitaciones y proponer recomendaciones.

---

## 💡 Desarrollo del Caso

### 1. Análisis

**Ventajas de contenerizar una aplicación:**
- ✅ Portabilidad: La API funciona igual en cualquier entorno que soporte Docker.
- ✅ Consistencia: Misma versión de Node.js y dependencias en desarrollo, pruebas y producción.
- ✅ Facilidad de despliegue: Despliegues rápidos y repetibles con un solo comando.
- ✅ Escalabilidad horizontal: Múltiples instancias de la API pueden ejecutarse simultáneamente.
- ✅ Aislamiento: Las dependencias están encapsuladas, evitando conflictos.

**Limitaciones posibles:**
- ⚠️ Curva de aprendizaje: El equipo debe familiarizarse con Docker y sus conceptos.
- ⚠️ Complejidad en gestión: Gestionar múltiples contenedores puede ser complejo sin herramientas de orquestación.
- ⚠️ Overhead de recursos: Los contenedores consumen recursos adicionales del sistema.
- ⚠️ Dependencia de orquestadores: Para entornos complejos se requiere Docker Compose o Kubernetes

---

### 2. Implementación del Dockerfile

Ejemplo de **Dockerfile** para la API Node.js con Express:

``` dockerfile
# Usar imagen base oficial de Node.js (versión LTS)
FROM node:18-alpine

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /usr/src/app

# Copiar archivos de dependencias primero (para aprovechar cache de Docker)
COPY package*.json ./

# Instalar dependencias de producción
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

🔎 **Explicación:**\
- `FROM node:18-alpine`: Utiliza imagen ligera de Node.js basada en Alpine Linux.
- `WORKDIR`: Establece el directorio de trabajo dentro del contenedor.
- `COPY package*.json`: Copia archivos de dependencias primero para optimizar el cache.
- `RUN npm ci`: Instala dependencias de manera más eficiente que `npm install`.
- `RUN addgroup/adduser`: Crea usuario no privilegiado por seguridad.
- `COPY --chown`: Copia código fuente con permisos adecuados.
- `USER`: Cambia a usuario no privilegiado.
- `EXPOSE 3000`: Documenta que la API escucha en puerto 3000.
- `CMD`: Comando para iniciar la aplicación Express.

---

### 3. Gestión de Volúmenes y Redes

**Volúmenes:**
- Permiten la persistencia de datos fuera del ciclo de vida del contenedor.
- Para APIs, útiles para logs, uploads de archivos, o bases de datos embebidas.

Ejemplo:

```bash
# Crear volumen para logs
docker volume create fintech-logs

# Ejecutar contenedor con volumen montado
docker run -d \
  -v fintech-logs:/usr/src/app/logs \
  -v /host/uploads:/usr/src/app/uploads \
  --name fintech-api \
  fintechplus-api
```

**Redes:**
- Docker crea redes virtuales para conectar contenedores entre sí y con el host.
- Esencial para comunicación entre la API y bases de datos.

Ejemplo:

```bash
# Crear red personalizada
docker network create fintech-network

# Ejecutar base de datos MongoDB
docker run -d \
  --name fintech-db \
  --network fintech-network \
  -e MONGO_INITDB_ROOT_USERNAME=admin \
  -e MONGO_INITDB_ROOT_PASSWORD=password123 \
  mongo:5

# Ejecutar API conectada a la red
docker run -d \
  --name fintech-api \
  --network fintech-network \
  -p 3000:3000 \
  -e DATABASE_URL=mongodb://admin:password123@fintech-db:27017/fintechdb \
  fintechplus-api
```

Ejemplo con Docker Compose:

```yaml
version: '3.8'
services:
  api:
    build: .
    ports:
      - "3000:3000"
    volumes:
      - ./logs:/usr/src/app/logs
      - uploads:/usr/src/app/uploads
    networks:
      - fintech-network
    environment:
      - NODE_ENV=production
      - DATABASE_URL=mongodb://admin:password123@database:27017/fintechdb
    depends_on:
      - database

  database:
    image: mongo:5
    environment:
      - MONGO_INITDB_ROOT_USERNAME=admin
      - MONGO_INITDB_ROOT_PASSWORD=password123
    volumes:
      - mongo-data:/data/db
    networks:
      - fintech-network

volumes:
  uploads:
  mongo-data:

networks:
  fintech-network:
    driver: bridge
```

---

### 4. Reflexión

La **contenerización con Docker** aporta grandes beneficios:
- Escalabilidad mejorada gracias a la ejecución de múltiples instancias
balanceadas.
- Mayor consistencia entre entornos, evitando errores de configuración
manual.
- Reducción del tiempo de despliegue.

**Retos encontrados:**
- Gestión de múltiples contenedores (solucionable con Docker Compose o
Kubernetes).
- Necesidad de capacitar al equipo en Docker.

**Recomendaciones:**
- Adoptar **Docker Compose** para gestionar entornos de desarrollo y
pruebas.
- Migrar gradualmente a un orquestador como **Kubernetes** para
producción.
- Implementar buenas prácticas de seguridad (imágenes oficiales, escaneo
de vulnerabilidades).

---

## 📊 Diagrama de Arquitectura

``` mermaid
flowchart TD
    A[API Node.js Monolítica en Servidor Local] -->|Migración| B[Contenedor Docker - API Express]
    B --> C[Volumen Logs]
    B --> D[Volumen Uploads]
    B --> E[Red Docker - fintech-network]
    E --> F[Contenedor MongoDB]
    E --> G[Load Balancer]
    G --> H[Múltiples Instancias API]
    B --> I[Puerto 3000 - Host]
    
    subgraph "Entorno Contenerizado"
        B
        C
        D
        F
        H
    end
    
    subgraph "Comunicación Externa"
        I --> J[Clientes/Frontend]
        I --> K[Servicios Externos]
    end
```

Este diagrama ilustra cómo la API monolítica de Node.js se ejecuta en un **Contenedor Docker** con persistencia de datos, conectividad en red, y capacidad de escalamiento horizontal.

---

# 🚀 Desarrollo Práctico

## **1. Seciruty Group**:
### ecs-sg-fin-tech-plus
- **Name**: ecs-sg-fin-tech-plus
- **Description**: Acceso FinTechPlus
- **VPC**: default
- **Inbound rules**:
  - SSH
    - Type: SSH
    - Protocol: TCP
    - Port range: 22
    - Destination type: Anywhere-IPv4
    - Destination: 0.0.0.0/0
    - Description: Acceso SSH
  - TCP
    - Type: Custom TCP
    - Protocol: TCP
    - Port range: 3000
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

## **2. ECR**: Elastic Container Registry
## Repositorio
- **Repository name**: fin-tech-plus-repo
- **Image tag mutability**: Mutable
- **Encryption configuration**: AES-256

Dentro de `fin-tech-plus-repo` obtener los comandos `View push commands` para crear la imagen docker en el repositorio.

---

## **3. FinTechPlusApi**: Node + Express
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

## **5. ECS**: Elastic Container Service
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
