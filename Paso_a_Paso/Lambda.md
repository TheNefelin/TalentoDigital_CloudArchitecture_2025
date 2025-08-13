## **Lambda**: Relational Database Service
### Lambda S3 image
- **Function name**: artema-lambda-img
- **Runtime**: Python 3.13
- **Architecture**: x86_64
- **Execution role**: LabRole
- **VPC**: artema-vpc
- **Subnets**
    - artema-subnet-private2-us-east-1a
    - artema-subnet-private2-us-east-1b
- **Security groups**: artema-sg-lambda-img

### Environment variable
- **S3_BUCKET_NAME**: artema-s3-storage

```python
import boto3
import os

def lambda_handler(event, context):
    bucket_name = os.environ['S3_BUCKET_NAME']
    
    image_name = event.get('pathParameters', {}).get('image-name')

    if not image_name:
        return {
            'statusCode': 400,
            'body': "Error: Falta el parámetro 'image' en el query string."
        }
    
    if not image_name.lower().endswith('.webp'):
        return {
            'statusCode': 400,
            'body': "Error: Solo se permiten archivos con extensión .webp."
        }
    
    image_key = f"img/{image_name}"
    s3 = boto3.client('s3', region_name='us-east-1')
    
    try:
        s3.head_object(Bucket=bucket_name, Key=image_key)
        
        presigned_url = s3.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket_name, 'Key': image_key},
            ExpiresIn=3600  # 1 hora de validez
        )
        
        return {
            'statusCode': 302,
            'headers': {
                'Location': presigned_url
            }
        }
    
    except s3.exceptions.ClientError as e:
        if e.response['Error']['Code'] == '404':
            return {
                'statusCode': 404,
                'body': f"Error: El archivo '{image_name}' no existe en el bucket."
            }
        else:
            return {
                'statusCode': 500,
                'body': f"Error interno: {str(e)}"
            }
```

```json
{
  "pathParameters": {
    "image-name": "hisoka.webp"
  }
}
```

---

### Lambda RDS
- **Function name**: artema-lambda-rds
- **Runtime**: Python 3.13
- **Architecture**: x86_64
- **Execution role**: LabRole
- **VPC**: artema-vpc
- **Subnets**
    - artema-subnet-private2-us-east-1a
    - artema-subnet-private2-us-east-1b
- **Security groups**: artema-sg-lambda-rds

### Environment variable
- **DB_HOST**: rds-host
- **DB_PORT**: 5432
- **DB_NAME**: postgres
- **DB_USER**: postgres
- **DB_PASS**: *****
- **URI**: https://6ga2qyue32.execute-api.us-east-1.amazonaws.com/img/

### psycopg2-binary
- Es una versión empaquetada de psycopg2 (con los binarios incluidos) que facilita su instalación sin compilar.

1. crear projecto puthon vscode
```
lambda-psycopg2-layer/
```
2. instalar pg8000
```bash
pip install pg8000 -t python
```
```
lambda-psycopg2-layer/
  └── python
```
3. comprimir la carpeta python
```
- python -> python.zip
```
4. subir python.zip a layer para lambda (py-pg8000-layer)
    - **Name**: py-pg8000-layer
    - **Description**: Capa para conexión a PostgreSQL desde Lambda usando pg8000 
    - **Upload a .zip file**: python.zip
    - **Compatible architectures**: x86_64
    - **Compatible runtimes**: Python 3.13
5. agregar layer a lambda (py-pg8000-layer)
    - **Custom layers**: py-pg8000-layer
    - **Version**: 1

```python
import os
import json
import pg8000.native
from decimal import Decimal

def lambda_handler(event, context):
    DB_HOST = os.environ['DB_HOST']
    DB_PORT = os.environ['DB_PORT']
    DB_NAME = os.environ['DB_NAME']
    DB_USER = os.environ['DB_USER']
    DB_PASS = os.environ['DB_PASS']

    try:
        conn = pg8000.native.Connection(
            host=DB_HOST,
            port=DB_PORT,         
            database=DB_NAME,   
            user=DB_USER,
            password=DB_PASS,            
        )
        
        rows = conn.run("SELECT * FROM personajes_hxh")
        columns = [desc["name"] for desc in conn.columns]
        result = [dict(zip(columns, row)) for row in rows]
        
        conn.close()

        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps(result, default=decimal_handler)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

def decimal_handler(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError
```

---

### Lambda SQS Processor
- **Name**: artema-lambda-sqs-processor
- **Runtime**: Python 3.13
- **Architecture**: x86_64
- **Use an existing role**: LabRole
- **VPC**: artema-vpc
- **Subnets**
    - artema-subnet-private1-us-east-1a
    - artema-subnet-private2-us-east-1b
- **Security groups**: artema-sg-lambda

###  Configuration - Environment variable
- **RDS_ENDPOINT**: artema-pgdb.code.us-east-1.rds.amazonaws.com
- **DB_NAME**: postgres
- **SNS_TOPIC_ARN**: arn:aws:sns:us-east-1:account:artema-sns

```python
import json
import boto3
import psycopg2
import os
from datetime import datetime

def lambda_handler(event, context):
  # Clientes AWS
  sns = boto3.client('sns')
  
  # Procesar mensajes de SQS
  for record in event['Records']:
    try:
      # Parsear mensaje
      message = json.loads(record['body'])
      
      # Conectar a RDS
      conn = psycopg2.connect(
        host=os.environ['RDS_ENDPOINT'],
        database=os.environ['DB_NAME'],
        user='postgres',
        password='tu_password_aqui'  # Mejor usar AWS Secrets Manager
      )
      
      # Insertar log de procesamiento
      cur = conn.cursor()
      cur.execute("""
        INSERT INTO processing_logs (message_id, content, processed_at) 
        VALUES (%s, %s, %s)
      """, (record['messageId'], str(message), datetime.now()))
      
      conn.commit()
      cur.close()
      conn.close()
      
      # Enviar notificación
      sns.publish(
        TopicArn=os.environ['SNS_TOPIC_ARN'],
        Subject='Mensaje Procesado',
        Message=f'Mensaje {record["messageId"]} procesado exitosamente'
      )
        
    except Exception as e:
      print(f"Error procesando mensaje: {str(e)}")
      # El mensaje volverá a SQS para reintento
      raise e
  
  return {
    'statusCode': 200,
    'body': json.dumps('Mensajes procesados exitosamente')
  }
```

---

### Lambda Auto Scaling Notification Handler
- **Name**: artema-lambda-asg-notifications
- **Runtime**: Python 3.13
- **Architecture**: x86_64
- **Use an existing role**: LabRole
- **VPC**: artema-vpc
- **Subnets**
    - artema-subnet-private1-us-east-1a
    - artema-subnet-private2-us-east-1b
- **Security groups**: artema-sg-lambda

### Configuration - Triggers
- **Trigger configuration**: 
- **SQS queue**: 
- **Batch size**: 1
- **Batch window**: 0

```python
import json
import boto3
from datetime import datetime

def lambda_handler(event, context):
  sns = boto3.client('sns')
  
  for record in event['Records']:
    # Parsear notificación de Auto Scaling
    message = json.loads(record['body'])
    
    # Extraer información relevante
    if 'AutoScalingGroupName' in str(message):
      notification_type = message.get('Event', 'Unknown')
      instance_id = message.get('EC2InstanceId', 'Unknown')
      
      # Enviar notificación personalizada
      sns.publish(
        TopicArn='arn:aws:sns:us-east-1:account:artema-sns',
        Subject=f'Auto Scaling Event: {notification_type}',
        Message=f"""
        Evento de Auto Scaling detectado:
        - Tipo: {notification_type}
        - Instancia: {instance_id}
        - Hora: {datetime.now()}
        - Grupo: artema-asg
        """
      )
  
  return {'statusCode': 200}
```

### IAM Permissions (Anexar a LabRole o crear role específico)
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "sqs:ReceiveMessage",
        "sqs:DeleteMessage",
        "sqs:GetQueueAttributes"
      ],
      "Resource": "arn:aws:sqs:us-east-1:account:artema-sqs-*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "sns:Publish"
      ],
      "Resource": "arn:aws:sns:us-east-1:account:artema-sns"
    },
    {
      "Effect": "Allow",
      "Action": [
        "rds:DescribeDBInstances"
      ],
      "Resource": "*"
    }
  ]
}
```

---
