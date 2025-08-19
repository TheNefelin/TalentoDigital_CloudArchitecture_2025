import json
import boto3
import os

# Configuración del cliente SQS (no se usa directamente en este código, pero es buena práctica)
sqs_client = boto3.client('sqs')

def lambda_handler(event, context):
    """
    Función que procesa mensajes de una cola SQS, activada por la propia cola.
    """
    # En lugar de usar event['Records'] directamente, usamos .get() para evitar el error si la clave no existe.
    records = event.get('Records', [])
    
    # Si el evento no tiene el formato de SQS (por ejemplo, en un test manual sin la plantilla correcta),
    # records será una lista vacía y no se ejecutará el bucle.
    if not records:
        print("Evento recibido no tiene el formato de SQS. No hay registros para procesar.")
        return {
            'statusCode': 200,
            'body': json.dumps('No hay registros para procesar.')
        }

    for record in records:
        try:
            # Extraer el cuerpo y el ID del mensaje
            message_body = record['body']
            message_id = record['messageId']

            print(f"✅ Procesando mensaje. ID: {message_id}, Cuerpo: {message_body}")
            
            # Aquí va tu lógica de negocio para procesar el mensaje.
            # Por ejemplo, guardar datos en DynamoDB, invocar otra Lambda, etc.
            
            # NOTA IMPORTANTE:
            # Cuando una Lambda es disparada por SQS, AWS se encarga de eliminar el
            # mensaje de la cola automáticamente si la ejecución de la función termina con éxito.
            
        except KeyError as e:
            print(f"❌ Error de formato en el mensaje recibido. Falta la clave: {e}")
        except Exception as e:
            print(f"❌ Ocurrió un error inesperado al procesar el mensaje: {e}")
            # Si la Lambda falla, el mensaje vuelve a la cola y SQS lo reintenta.
    
    return {
        'statusCode': 200,
        'body': json.dumps('Mensajes procesados exitosamente.')
    }