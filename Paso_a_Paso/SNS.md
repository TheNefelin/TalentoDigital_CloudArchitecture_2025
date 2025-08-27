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

## **SNS**: Simple Notification Service 
### Topics
- **Topics**: Standard
- **Name**: monolito-sns-webapi

### Create subscription
- **Topic ARN**: monolito-sns-webapi
- **Protocol**: Amazon SQS
- **Endpoint**: monolito-sqs-worker

> Obtener ARN para la variable de entorno

- Subscription filter policy (email)
```json
{
 "action": [
    "process",
    "generate_pdf"
 ]
}
```
- Subscription filter policy (worker)
```json
{
  "target": [
    "test@email.com",
    "all"
  ]
}
```
