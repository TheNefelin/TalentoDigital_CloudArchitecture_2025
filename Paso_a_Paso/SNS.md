## **SNS**: Simple Notification Service 
### Topics
- **Topics**: Standard
- **Name**: artema-sns

### Create subscription
- **Topic ARN**: artema-sns
- **Protocol**: mail@mail.cl

---

## **SQS**: Simple Queue Service:
### Create queue
- **Type**: Standard
- **Name**: monolitica-sqs
- **Visibility timeout**: 30 Seconds
- **Message retention period**: 4 Days
- **Delivery delay**: 0
- **Receive message wait time**: 0
- **Maximum message size**: 1024 KiB

> Obtener URL para la variable de entorno

## **SNS**: Simple Notification Service 
### Topics
- **Topics**: Standard
- **Name**: monolitica-sns

### Create subscription
- **Topic ARN**: monolitica-sns
- **Protocol**: Amazon SQS
- **Endpoint**: monolitica-sqs

### Create subscription
- **Topic ARN**: monolitica-sns-clone
- **Protocol**: Amazon SQS
- **Endpoint**: monolitica-sqs

> Obtener ARN para la variable de entorno

---