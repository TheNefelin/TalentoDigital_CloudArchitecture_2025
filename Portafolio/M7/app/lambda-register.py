import boto3
import json
import os
import hmac
import hashlib
import base64

def calculate_secret_hash(username, client_id, client_secret):
    message = username + client_id
    dig = hmac.new(
        client_secret.encode('utf-8'),
        msg=message.encode('utf-8'),
        digestmod=hashlib.sha256
    ).digest()
    return base64.b64encode(dig).decode()

def lambda_handler(event, context):
    client = boto3.client('cognito-idp')
    
    CLIENT_ID = os.environ['COGNITO_CLIENT_ID']
    CLIENT_SECRET = os.environ['COGNITO_CLIENT_SECRET']
    USER_POOL_ID = os.environ['COGNITO_USER_POOL_ID']
    
    body = json.loads(event['body'])
    email = body['email']
    password = body['password']
    
    secret_hash = calculate_secret_hash(email, CLIENT_ID, CLIENT_SECRET)
    
    try:
        # 1. Registrar usuario
        response = client.sign_up(
            ClientId=CLIENT_ID,
            Username=email,
            Password=password,
            SecretHash=secret_hash,
            UserAttributes=[{'Name': 'email', 'Value': email}]
        )
        
        # 2. ✅ VERIFICAR ADMINISTRATIVAMENTE (sin código)
        client.admin_confirm_sign_up(
            UserPoolId=USER_POOL_ID,
            Username=email
        )
        
        # 3. ✅ MARCAR EMAIL COMO VERIFICADO
        client.admin_update_user_attributes(
            UserPoolId=USER_POOL_ID,
            Username=email,
            UserAttributes=[
                {'Name': 'email_verified', 'Value': 'true'}
            ]
        )
        
        return {
            'statusCode': 200,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({
                'message': 'Usuario registrado y verificado automáticamente',
                'userSub': response['UserSub']
            })
        }
        
    except client.exceptions.UsernameExistsException:
        return {
            'statusCode': 400,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': 'El usuario ya existe'})
        }
    except Exception as e:
        return {
            'statusCode': 400,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': str(e)})
        }