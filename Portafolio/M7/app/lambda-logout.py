import boto3
import json
import os
import hmac
import hashlib
import base64

def calculate_secret_hash(username, client_id, client_secret):
    """
    Calcula el SECRET_HASH requerido por Cognito cuando el cliente tiene Client Secret
    """
    message = username + client_id
    dig = hmac.new(
        client_secret.encode('utf-8'),
        msg=message.encode('utf-8'),
        digestmod=hashlib.sha256
    ).digest()
    return base64.b64encode(dig).decode()

def lambda_handler(event, context):
    client = boto3.client('cognito-idp')
    
    # Variables de entorno (las mismas que en login/register)
    CLIENT_ID = os.environ['COGNITO_CLIENT_ID']
    CLIENT_SECRET = os.environ['COGNITO_CLIENT_SECRET']
    USER_POOL_ID = os.environ['COGNITO_USER_POOL_ID']
    
    try:
        # Parsear el body de la request
        body = json.loads(event['body'])
        
        # Opción 1: Logout con email (requiere SECRET_HASH)
        if 'email' in body:
            email = body['email']
            secret_hash = calculate_secret_hash(email, CLIENT_ID, CLIENT_SECRET)
            
            # Logout global del usuario (invalida todos los tokens)
            response = client.admin_user_global_sign_out(
                UserPoolId=USER_POOL_ID,
                Username=email
            )
            
            return {
                'statusCode': 200,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Content-Type': 'application/json'
                },
                'body': json.dumps({
                    'message': 'Logout exitoso. Todos los tokens han sido invalidados.',
                    'method': 'global_sign_out'
                })
            }
        
        # Opción 2: Logout con access_token (más común en frontends)
        elif 'access_token' in body:
            access_token = body['access_token']
            
            # Logout con token específico
            response = client.global_sign_out(
                AccessToken=access_token
            )
            
            return {
                'statusCode': 200,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Content-Type': 'application/json'
                },
                'body': json.dumps({
                    'message': 'Logout exitoso. Token invalidado.',
                    'method': 'token_sign_out'
                })
            }
        
        else:
            return {
                'statusCode': 400,
                'headers': {'Access-Control-Allow-Origin': '*'},
                'body': json.dumps({
                    'error': 'Se requiere "email" o "access_token" para hacer logout'
                })
            }
    
    except client.exceptions.NotAuthorizedException:
        return {
            'statusCode': 401,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': 'Token inválido o expirado'})
        }
    
    except client.exceptions.UserNotFoundException:
        return {
            'statusCode': 404,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': 'Usuario no encontrado'})
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
            'body': json.dumps({'error': f'Campo requerido faltante: {str(e)}'})
        }
    
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': f'Error interno del servidor: {str(e)}'})
        }