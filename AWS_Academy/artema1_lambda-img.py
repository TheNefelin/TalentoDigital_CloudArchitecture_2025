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