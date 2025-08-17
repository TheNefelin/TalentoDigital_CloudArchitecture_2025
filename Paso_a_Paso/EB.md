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