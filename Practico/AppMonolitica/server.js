const express = require('express');
const AWS = require('aws-sdk');
const YAML = require('yamljs');
const swaggerUi = require('swagger-ui-express');
require('dotenv').config();

const app = express();
const port = process.env.PORT || 3000;

// Middleware básico
app.use(express.json());

// Configurar Swagger
try {
  const swaggerDocument = YAML.load('./swagger.yaml');
  app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerDocument));
  console.log('📚 Swagger configurado en /api-docs');
} catch (error) {
  console.log('⚠️  Swagger no disponible - archivo swagger.yaml no encontrado');
}

// Configurar AWS
AWS.config.update({
  region: process.env.AWS_REGION || 'us-east-1'
});

const sns = new AWS.SNS();
const sqs = new AWS.SQS();

// Variables
const SNS_TOPIC_ARN = process.env.SNS_TOPIC_ARN;
const SQS_QUEUE_URL = process.env.SQS_QUEUE_URL;

// Ruta básica
app.get('/', (req, res) => {
  res.json({ 
    message: 'API de Mensajería - SQS & SNS',
    endpoints: [
      'GET /health',
      'POST /sns/publish', 
      'POST /sqs/send',
      'GET /sqs/receive'
    ]
  });
});

// Health check
app.get('/health', (req, res) => {
  res.json({ status: 'OK', timestamp: new Date().toISOString() });
});

// Publicar en SNS
app.post('/sns/publish', async (req, res) => {
  try {
    const { message, subject } = req.body;
    
    if (!message) {
      return res.status(400).json({ error: 'Mensaje requerido' });
    }

    const result = await sns.publish({
      TopicArn: SNS_TOPIC_ARN,
      Message: message,
      Subject: subject || 'Notificación'
    }).promise();

    res.json({ success: true, messageId: result.MessageId });
  } catch (error) {
    console.error('Error SNS:', error);
    res.status(500).json({ error: error.message });
  }
});

// Enviar a SQS
app.post('/sqs/send', async (req, res) => {
  try {
    const { message } = req.body;
    
    if (!message) {
      return res.status(400).json({ error: 'Mensaje requerido' });
    }

    const result = await sqs.sendMessage({
      QueueUrl: SQS_QUEUE_URL,
      MessageBody: message
    }).promise();

    res.json({ success: true, messageId: result.MessageId });
  } catch (error) {
    console.error('Error SQS Send:', error);
    res.status(500).json({ error: error.message });
  }
});

// Recibir de SQS
app.get('/sqs/receive', async (req, res) => {
  try {
    const result = await sqs.receiveMessage({
      QueueUrl: SQS_QUEUE_URL,
      MaxNumberOfMessages: 10
    }).promise();

    const messages = result.Messages || [];

    // Eliminar mensajes después de recibirlos
    for (const msg of messages) {
      await sqs.deleteMessage({
        QueueUrl: SQS_QUEUE_URL,
        ReceiptHandle: msg.ReceiptHandle
      }).promise();
    }

    res.json({ 
      success: true, 
      messages: messages.map(m => ({ id: m.MessageId, body: m.Body })),
      count: messages.length 
    });
  } catch (error) {
    console.error('Error SQS Receive:', error);
    res.status(500).json({ error: error.message });
  }
});

app.listen(port, () => {
  console.log(`🚀 API corriendo en puerto ${port}`);
  console.log(`📍 Prueba: http://localhost:${port}`);
  console.log(`📍 Swagger: http://localhost:${port}/api-docs`);
});
