## **DynamoDB**:
### Tables - User
- **Table name**: inventario-ddb
- **Partition key**: id Number
- **Create Table**:

```json
{
  "id": {"N": "1"},
  "nombre": {"S": "Producto Ejemplo"},
  "cantidad": {"N": "25"},
  "precio": {"N": "29.99"}
}
```

## **S3 Bucket**: Almacenamiento Estático
### Bucket
- **Name**: inventario-s3-storage-01
- **Object Ownership**: ACLs desactivados
- **Block all public access**: check
- **Versioning**: Disable
- **Encryption**: SSE-S3
- **Bucket Key**: Disable
### Properties - Event notifications
- **Event name**: load-file-s3
- **All object create events**:  check
### Permissions - Bucket Policy
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::992136605746:role/LabRole"
      },
      "Action": [
        "s3:GetObject",
        "s3:ListBucket",
        "s3:PutObject"
      ],
      "Resource": [
        "arn:aws:s3:::inventario-s3-storage-01",
        "arn:aws:s3:::inventario-s3-storage-01/*"
      ]
    }
  ]
}
```
### Upload inventario.json
```json
[
  {
    "id": {"N": "1"},
    "nombre": {"S": "Producto Ejemplo"},
    "cantidad": {"N": "25"},
    "precio": {"N": "29.99"}
  },
  {
    "id": {"N": "2"},
    "nombre": {"S": "Teclado Mecánico"},
    "cantidad": {"N": "15"},
    "precio": {"N": "89.99"}
  },
  {
    "id": {"N": "3"},
    "nombre": {"S": "Monitor 24 pulgadas"},
    "cantidad": {"N": "8"},
    "precio": {"N": "199.99"}
  },
  {
    "id": {"N": "4"},
    "nombre": {"S": "Mouse Inalámbrico"},
    "cantidad": {"N": "35"},
    "precio": {"N": "24.50"}
  },
  {
    "id": {"N": "5"},
    "nombre": {"S": "Auriculares Gaming"},
    "cantidad": {"N": "12"},
    "precio": {"N": "79.99"}
  }
]
```

### Lambda from-s3-to-ddb
- **Function name**: lambda-from-s3-to-ddb
- **Runtime**: Python 3.13
- **Architecture**: x86_64
- **Execution role**: LabRole
```py
import json, urllib, boto3, os

# Connect to S3 and DynamoDB
s3 = boto3.resource('s3')
dynamodb = boto3.resource('dynamodb')

# Connect to the DynamoDB table
inventoryTable = dynamodb.Table('Inventory')

def lambda_handler(event, context):
    # Show the incoming event
    print("Event received by Lambda function: " + json.dumps(event, indent=2))
    
    # Get the bucket and object key
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
    localFilename = '/tmp/inventory.json'
    
    # Download the file from S3
    try:
        s3.meta.client.download_file(bucket, key, localFilename)
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e
    
    # Read and parse the JSON file
    try:
        with open(localFilename, 'r') as json_file:
            data = json.load(json_file)
    except Exception as e:
        print(f"Error parsing JSON file: {str(e)}")
        raise e
    
    # Process the JSON data
    rowCount = 0
    try:
        # Check if data is a list (array) or a single object
        if isinstance(data, list):
            # Process multiple items
            for item in data:
                rowCount += 1
                print(f"Inserting item {rowCount}: {item}")
                
                # Insert into DynamoDB - AJUSTA ESTOS CAMPOS SEGÚN TU ESQUEMA
                inventoryTable.put_item(
                    Item={
                        'id': str(item['id']),
                        'nombre': item['nombre'],
                        'cantidad': int(item['cantidad']),
                        'precio': float(item['precio'])
                    }
                )
                
        elif isinstance(data, dict):
            # Process single item
            rowCount = 1
            print(f"Inserting single item: {data}")
            
            # Insert into DynamoDB - AJUSTA ESTOS CAMPOS SEGÚN TU ESQUEMA
            inventoryTable.put_item(
                Item={
                    'id': str(data['id']),
                    'nombre': data['nombre'],
                    'cantidad': int(data['cantidad']),
                    'precio': float(data['precio'])
                }
            )
            
        else:
            raise ValueError("Invalid JSON format. Expected object or array.")
            
    except Exception as e:
        print(f"Error inserting data into DynamoDB: {str(e)}")
        raise e
    
    # Finished!
    return f"{rowCount} items inserted into DynamoDB"
```


```py
import json, urllib, boto3, os

# Connect to S3 and DynamoDB
s3 = boto3.resource('s3')
dynamodb = boto3.resource('dynamodb')

# Connect to the DynamoDB table
inventoryTable = dynamodb.Table('inventario-s3-storage-01')

def lambda_handler(event, context):
    # Show the incoming event
    print("Event received by Lambda function: " + json.dumps(event, indent=2))
    
    # Get the bucket and object key
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
    localFilename = '/tmp/inventory.json'
    
    # Download the file from S3
    try:
        s3.meta.client.download_file(bucket, key, localFilename)
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e
    
    # Read and parse the JSON file
    try:
        with open(localFilename, 'r') as json_file:
            data = json.load(json_file)
    except Exception as e:
        print(f"Error parsing JSON file: {str(e)}")
        raise e
    
    # Process the JSON data
    rowCount = 0
    try:
        # Check if data is a list (array) or a single object
        if isinstance(data, list):
            # Process multiple items
            for item in data:
                rowCount += 1
                print(f"Inserting item {rowCount}: {item}")
                
                # Insert into DynamoDB - AJUSTA ESTOS CAMPOS SEGÚN TU ESQUEMA
                inventoryTable.put_item(
                    Item={
                        'id': str(item['id']),
                        'nombre': item['nombre'],
                        'cantidad': int(item['cantidad']),
                        'precio': float(item['precio'])
                    }
                )
                
        elif isinstance(data, dict):
            # Process single item
            rowCount = 1
            print(f"Inserting single item: {data}")
            
            # Insert into DynamoDB - AJUSTA ESTOS CAMPOS SEGÚN TU ESQUEMA
            inventoryTable.put_item(
                Item={
                    'id': str(data['id']),
                    'nombre': data['nombre'],
                    'cantidad': int(data['cantidad']),
                    'precio': float(data['precio'])
                }
            )
            
        else:
            raise ValueError("Invalid JSON format. Expected object or array.")
            
    except Exception as e:
        print(f"Error inserting data into DynamoDB: {str(e)}")
        raise e
    
    # Finished!
    return f"{rowCount} items inserted into DynamoDB"
```

## **SNS**: Simple Notification Service 
### Topics
- **Topics**: Standard
- **Name**: NoStock

### Create subscription
- **Topic ARN**: artema-sns
- **Protocol**: mail@mail.cl

---

### Lambda notification stock
- **Function name**: lambda-notification-strock
- **Runtime**: Python 3.13
- **Architecture**: x86_64
- **Execution role**: LabRole
```py

```


```py
# Load-Inventory Lambda function
#
# This function is triggered by an object being created in an Amazon S3 bucket.
# The file is downloaded and each line is inserted into a DynamoDB table.
import json, urllib, boto3, csv
# Connect to S3 and DynamoDB
s3 = boto3.resource('s3')
dynamodb = boto3.resource('dynamodb')
# Connect to the DynamoDB tables
inventoryTable = dynamodb.Table('Inventory');
# This handler is run every time the Lambda function is triggered
def lambda_handler(event, context):
  # Show the incoming event in the debug log
  print("Event received by Lambda function: " + json.dumps(event, indent=2))
  # Get the bucket and object key from the Event
  bucket = event['Records'][0]['s3']['bucket']['name']
  key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
  localFilename = '/tmp/inventory.txt'
  # Download the file from S3 to the local filesystem
  try:
    s3.meta.client.download_file(bucket, key, localFilename)
  except Exception as e:
    print(e)
    print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
    raise e
  # Read the Inventory CSV file
  with open(localFilename) as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    # Read each row in the file
    rowCount = 0
    for row in reader:
      rowCount += 1
      # Show the row in the debug log
      print(row['store'], row['item'], row['count'])
      try:
        # Insert Store, Item and Count into the Inventory table
        inventoryTable.put_item(
          Item={
            'Store':  row['store'],
            'Item':   row['item'],
            'Count':  int(row['count'])})
      except Exception as e:
         print(e)
         print("Unable to insert data into DynamoDB table".format(e))
    # Finished!
    return "%d counts inserted" % rowCount
Paulo Berrios
10:45 p.m.
# Stock Check Lambda function
#
# This function is triggered when values are inserted into the Inventory DynamoDB table.
# Inventory counts are checked and if an item is out of stock, a notification is sent to an SNS Topic.
import json, boto3
# This handler is run every time the Lambda function is triggered
def lambda_handler(event, context):
  # Show the incoming event in the debug log
  print("Event received by Lambda function: " + json.dumps(event, indent=2))
  # For each inventory item added, check if the count is zero
  for record in event['Records']:
    newImage = record['dynamodb'].get('NewImage', None)
    if newImage:      
      count = int(record['dynamodb']['NewImage']['Count']['N'])  
      if count == 0:
        store = record['dynamodb']['NewImage']['Store']['S']
        item  = record['dynamodb']['NewImage']['Item']['S']  
        # Construct message to be sent
        message = store + ' is out of stock of ' + item
        print(message)  
        # Connect to SNS
        sns = boto3.client('sns')
        alertTopic = 'NoStock'
        snsTopicArn = [t['TopicArn'] for t in sns.list_topics()['Topics']
                        if t['TopicArn'].lower().endswith(':' + alertTopic.lower())][0]  
        # Send message to SNS
        sns.publish(
          TopicArn=snsTopicArn,
          Message=message,
          Subject='Inventory Alert!',
          MessageStructure='raw'
        )
  # Finished!
  return 'Successfully processed {} records.'.format(len(event['Records']))
```

```py
# Load-Inventory Lambda function
#
# This function is triggered by an object being created in an Amazon S3 bucket.
# The file is downloaded and each line is inserted into a DynamoDB table.
import json, urllib, boto3, csv
# Connect to S3 and DynamoDB
s3 = boto3.resource('s3')
dynamodb = boto3.resource('dynamodb')
# Connect to the DynamoDB tables
inventoryTable = dynamodb.Table('Inventory');
# This handler is run every time the Lambda function is triggered
def lambda_handler(event, context):
  # Show the incoming event in the debug log
  print("Event received by Lambda function: " + json.dumps(event, indent=2))
  # Get the bucket and object key from the Event
  bucket = event['Records'][0]['s3']['bucket']['name']
  key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
  localFilename = '/tmp/inventory.txt'
  # Download the file from S3 to the local filesystem
  try:
    s3.meta.client.download_file(bucket, key, localFilename)
  except Exception as e:
    print(e)
    print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
    raise e
  # Read the Inventory CSV file
  with open(localFilename) as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    # Read each row in the file
    rowCount = 0
    for row in reader:
      rowCount += 1
      # Show the row in the debug log
      print(row['store'], row['item'], row['count'])
      try:
        # Insert Store, Item and Count into the Inventory table
        inventoryTable.put_item(
          Item={
            'Store':  row['store'],
            'Item':   row['item'],
            'Count':  int(row['count'])})
      except Exception as e:
         print(e)
         print("Unable to insert data into DynamoDB table".format(e))
    # Finished!
    return "%d counts inserted" % rowCount
Paulo Berrios
22:26
# Load-Inventory Lambda function
#
# This function is triggered by an object being created in an Amazon S3 bucket.
# The file is downloaded and each line is inserted into a DynamoDB table.
import json, urllib, boto3, csv
# Connect to S3 and DynamoDB
s3 = boto3.resource('s3')
dynamodb = boto3.resource('dynamodb')
# Connect to the DynamoDB tables
inventoryTable = dynamodb.Table('Inventory');
# This handler is run every time the Lambda function is triggered
def lambda_handler(event, context):
  # Show the incoming event in the debug log
  print("Event received by Lambda function: " + json.dumps(event, indent=2))
  # Get the bucket and object key from the Event
  bucket = event['Records'][0]['s3']['bucket']['name']
  key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
  localFilename = '/tmp/inventory.txt'
  # Download the file from S3 to the local filesystem
  try:
    s3.meta.client.download_file(bucket, key, localFilename)
  except Exception as e:
    print(e)
    print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
    raise e
  # Read the Inventory CSV file
  with open(localFilename) as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    # Read each row in the file
    rowCount = 0
    for row in reader:
      rowCount += 1
      # Show the row in the debug log
      print(row['store'], row['item'], row['count'])
      try:
        # Insert Store, Item and Count into the Inventory table
        inventoryTable.put_item(
          Item={
            'Store':  row['store'],
            'Item':   row['item'],
            'Count':  int(row['count'])})
      except Exception as e:
         print(e)
         print("Unable to insert data into DynamoDB table".format(e))
    # Finished!
    return "%d counts inserted" % rowCount
```
