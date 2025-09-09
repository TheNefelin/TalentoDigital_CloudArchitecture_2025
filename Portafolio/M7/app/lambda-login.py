import boto3
import json
import os
import hmac
import hashlib
import base64

# Calcular SECRET_HASH (igual que en registro)
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
    
    # Obtener configuración desde variables de entorno
    CLIENT_ID = os.environ['COGNITO_CLIENT_ID']
    CLIENT_SECRET = os.environ['COGNITO_CLIENT_SECRET']
    USER_POOL_ID = os.environ['COGNITO_USER_POOL_ID']
    
    try:
        # Parsear el body de la request
        body = json.loads(event['body'])
        email = body['email']
        password = body['password']
        
        # Calcular secret hash (OBLIGATORIO porque tienes Client Secret)
        secret_hash = calculate_secret_hash(email, CLIENT_ID, CLIENT_SECRET)
        
        # Hacer login con Cognito
        response = client.admin_initiate_auth(
            UserPoolId=USER_POOL_ID,
            ClientId=CLIENT_ID,
            AuthFlow='ADMIN_NO_SRP_AUTH',
            AuthParameters={
                'USERNAME': email,
                'PASSWORD': password,
                'SECRET_HASH': secret_hash
            }
        )
        
        # Extraer tokens de la respuesta
        auth_result = response['AuthenticationResult']
        
        # Respuesta exitosa
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'message': 'Login exitoso',
                'access_token': auth_result['AccessToken'],
                'refresh_token': auth_result['RefreshToken'],
                'expires_in': auth_result['ExpiresIn'],
                'token_type': auth_result['TokenType']
            })
        }
        
    except client.exceptions.NotAuthorizedException:
        return {
            'statusCode': 401,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': 'Email o contraseña incorrectos'})
        }
    except client.exceptions.UserNotFoundException:
        return {
            'statusCode': 404,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': 'Usuario no encontrado'})
        }
    except client.exceptions.UserNotConfirmedException:
        return {
            'statusCode': 403,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': 'Usuario no verificado. Revisa tu email para verificar la cuenta.'})
        }
    except json.JSONDecodeError:
        return {
            'statusCode': 400,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': 'Formato de JSON inválido'})
        }
    except KeyError as e:
        return {
            'statusCode': 400,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': f'Falta campo requerido: {str(e)}'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': f'Error interno del servidor: {str(e)}'})
        }