## **EB**: Elastic Beanstalk
- **Web server environment**: chceck
- **Application name**: artema-eb-node
- **Platform**: Node.js
- **Platform branch**: Node.js 22 running on 64bit Amazon Linux 2023
- **Platform version**: 6.6.3

### Servidor Node + Express
```sh
npm init -y
```

```sh
npm install express @aws-sdk/client-sns @aws-sdk/client-sqs
```

```javascript
import express from "express";
import { SNSClient, PublishCommand } from "@aws-sdk/client-sns";
import { SQSClient, ReceiveMessageCommand, DeleteMessageCommand } from "@aws-sdk/client-sqs";

const app = express();
app.use(express.json());

// Configurar clientes AWS SDK v3
const sns = new SNSClient({ region: "us-east-1" });
const sqs = new SQSClient({ region: "us-east-1" });

const SNS_TOPIC_ARN = process.env.SNS_TOPIC_ARN; // Tema SNS
const SQS_URL = process.env.SQS_URL;             // URL de la cola

// Endpoint: publicar notificación SNS
app.post("/notify", async (req, res) => {
  const { message } = req.body;

  try {
    const command = new PublishCommand({
      TopicArn: SNS_TOPIC_ARN,
      Message: message,
    });
    await sns.send(command);
    res.json({ success: true, message: "Notificación enviada via SNS" });
  } catch (err) {
    console.error(err);
    res.status(500).json({ success: false, error: err.message });
  }
});

// Endpoint: leer mensajes de SQS
app.get("/messages", async (req, res) => {
  try {
    const command = new ReceiveMessageCommand({
      QueueUrl: SQS_URL,
      MaxNumberOfMessages: 5,
      WaitTimeSeconds: 5,
    });

    const response = await sqs.send(command);

    if (response.Messages) {
      for (let msg of response.Messages) {
        // Aquí procesarías el mensaje
        console.log("Procesando:", msg.Body);

        // Eliminarlo de la cola
        await sqs.send(new DeleteMessageCommand({
          QueueUrl: SQS_URL,
          ReceiptHandle: msg.ReceiptHandle
        }));
      }
    }

    res.json({ success: true, messages: response.Messages || [] });
  } catch (err) {
    console.error(err);
    res.status(500).json({ success: false, error: err.message });
  }
});

app.listen(8080, () => console.log("App corriendo en puerto 8080 🚀"));
```

---

## **EB**: Elastic Beanstalk
### Applications
- **Web server environment**: chceck
- **Application name**: fin-tech-plus-eb
- **Platform**: Node.js
- **Platform branch**: Node.js 22 running on 64bit Amazon Linux 2023
- **Platform version**: 6.6.3
- **Upload your code**: check
- **Version labe**: 1
- **Local file**: server.zip
- **Single instance**: check
- **Service role**: LabRole
- **EC2 instance profile**: LabInstanceProfile
- **EC2 key pair**: vockey
- **VPC**: default
- **Public IP address**: Enable
- **Instance subnets**:
  - us-east-1a
  - us-east-1b
- **EC2 security groups**: ecs-sg-fin-tech-plus
- **Health reporting**: Basic
- **Managed updates**: uncheck

### Estructura
```
artema-s3-storage/
├── package.json
├── package-lock.json
└── server.js
```

```sh
npm init -y
```

```sh
npm install express@4.18.2 cors uuid
```
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


---

