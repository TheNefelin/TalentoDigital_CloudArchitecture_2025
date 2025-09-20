import json
import boto3
import uuid
from datetime import datetime
from botocore.exceptions import ClientError

# Configuración DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('ticket-dydb')

def lambda_handler(event, context):
    """
    Lambda handler principal que maneja todas las operaciones CRUD
    """
    print("Event:", json.dumps(event, indent=2))
    
    http_method = event.get('httpMethod')
    resource = event.get('resource')
    path_parameters = event.get('pathParameters') or {}
    body = event.get('body')
    
    # Headers CORS
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, PUT, PATCH, DELETE, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type, Authorization'
    }
    
    try:
        # Manejar preflight requests
        if http_method == 'OPTIONS':
            return {
                'statusCode': 200,
                'headers': headers,
                'body': ''
            }
        
        # Routing basado en método HTTP y resource
        route = f"{http_method} {resource}"
        
        if route == 'POST /v1/tickets':
            return create_ticket(body, headers)
        
        elif route == 'GET /v1/tickets':
            return get_all_tickets(headers)
        
        elif route == 'GET /v1/tickets/{id}':
            return get_ticket(path_parameters.get('id'), headers)
        
        elif route == 'PUT /v1/tickets/{id}':
            return update_ticket(path_parameters.get('id'), body, headers, 'PUT')
        
        elif route == 'PATCH /v1/tickets/{id}':
            return update_ticket(path_parameters.get('id'), body, headers, 'PATCH')
        
        elif route == 'DELETE /v1/tickets/{id}':
            return delete_ticket(path_parameters.get('id'), headers)
        
        else:
            return {
                'statusCode': 404,
                'headers': headers,
                'body': json.dumps({
                    'error': 'Endpoint no encontrado',
                    'method': http_method,
                    'resource': resource
                })
            }
            
    except Exception as e:
        print(f"Error en lambda_handler: {str(e)}")
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({
                'error': 'Error interno del servidor',
                'message': str(e)
            })
        }

def create_ticket(body, headers):
    """
    Crear un nuevo ticket
    POST /v1/tickets
    """
    try:
        if not body:
            return {
                'statusCode': 400,
                'headers': headers,
                'body': json.dumps({'error': 'Body es requerido'})
            }
        
        ticket_data = json.loads(body)
        
        # Validar campos requeridos
        required_fields = ['title', 'description', 'status', 'reporterId']
        missing_fields = [field for field in required_fields if not ticket_data.get(field)]
        
        if missing_fields:
            return {
                'statusCode': 400,
                'headers': headers,
                'body': json.dumps({
                    'error': 'Campos requeridos faltantes',
                    'missingFields': missing_fields
                })
            }
        
        # Validar status
        valid_statuses = ['OPEN', 'IN_PROGRESS', 'CLOSED']
        if ticket_data['status'] not in valid_statuses:
            return {
                'statusCode': 400,
                'headers': headers,
                'body': json.dumps({
                    'error': f'Status inválido. Debe ser uno de: {", ".join(valid_statuses)}'
                })
            }
        
        # Crear ticket
        ticket_id = str(uuid.uuid4())
        timestamp = datetime.utcnow().isoformat() + 'Z'
        
        ticket = {
            'id': ticket_id,
            'title': ticket_data['title'],
            'description': ticket_data['description'],
            'status': ticket_data['status'],
            'reporterId': ticket_data['reporterId'],
            'createdAt': timestamp,
            'updatedAt': timestamp
        }
        
        # Guardar en DynamoDB
        table.put_item(Item=ticket)
        
        return {
            'statusCode': 201,
            'headers': headers,
            'body': json.dumps({
                'message': 'Ticket creado exitosamente',
                'ticket': ticket
            })
        }
        
    except json.JSONDecodeError:
        return {
            'statusCode': 400,
            'headers': headers,
            'body': json.dumps({'error': 'JSON inválido en el body'})
        }
    except ClientError as e:
        print(f"Error DynamoDB en create_ticket: {e}")
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({'error': 'Error al guardar en la base de datos'})
        }
    except Exception as e:
        print(f"Error en create_ticket: {e}")
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({'error': 'Error al crear el ticket'})
        }

def get_all_tickets(headers):
    """
    Obtener todos los tickets
    GET /v1/tickets
    """
    try:
        response = table.scan()
        tickets = response['Items']
        
        # Manejar paginación si hay más elementos
        while response.get('LastEvaluatedKey'):
            response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            tickets.extend(response['Items'])
        
        # Ordenar por fecha de creación (más reciente primero)
        tickets.sort(key=lambda x: x.get('createdAt', ''), reverse=True)
        
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({
                'tickets': tickets,
                'count': len(tickets)
            })
        }
        
    except ClientError as e:
        print(f"Error DynamoDB en get_all_tickets: {e}")
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({'error': 'Error al obtener tickets de la base de datos'})
        }
    except Exception as e:
        print(f"Error en get_all_tickets: {e}")
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({'error': 'Error al obtener los tickets'})
        }

def get_ticket(ticket_id, headers):
    """
    Obtener un ticket específico
    GET /v1/tickets/{id}
    """
    try:
        if not ticket_id:
            return {
                'statusCode': 400,
                'headers': headers,
                'body': json.dumps({'error': 'ID del ticket es requerido'})
            }
        
        response = table.get_item(Key={'id': ticket_id})
        
        if 'Item' not in response:
            return {
                'statusCode': 404,
                'headers': headers,
                'body': json.dumps({
                    'error': 'Ticket no encontrado',
                    'id': ticket_id
                })
            }
        
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({'ticket': response['Item']})
        }
        
    except ClientError as e:
        print(f"Error DynamoDB en get_ticket: {e}")
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({'error': 'Error al obtener ticket de la base de datos'})
        }
    except Exception as e:
        print(f"Error en get_ticket: {e}")
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({'error': 'Error al obtener el ticket'})
        }

def update_ticket(ticket_id, body, headers, method):
    """
    Actualizar un ticket
    PUT /v1/tickets/{id} - Reemplaza completamente
    PATCH /v1/tickets/{id} - Actualización parcial
    """
    try:
        if not ticket_id:
            return {
                'statusCode': 400,
                'headers': headers,
                'body': json.dumps({'error': 'ID del ticket es requerido'})
            }
        
        if not body:
            return {
                'statusCode': 400,
                'headers': headers,
                'body': json.dumps({'error': 'Body es requerido'})
            }
        
        update_data = json.loads(body)
        
        # Verificar que el ticket existe
        existing_ticket = table.get_item(Key={'id': ticket_id})
        if 'Item' not in existing_ticket:
            return {
                'statusCode': 404,
                'headers': headers,
                'body': json.dumps({
                    'error': 'Ticket no encontrado',
                    'id': ticket_id
                })
            }
        
        # Para PUT, validar campos requeridos
        if method == 'PUT':
            required_fields = ['title', 'description', 'status', 'reporterId']
            missing_fields = [field for field in required_fields if not update_data.get(field)]
            
            if missing_fields:
                return {
                    'statusCode': 400,
                    'headers': headers,
                    'body': json.dumps({
                        'error': 'Campos requeridos faltantes para PUT',
                        'missingFields': missing_fields
                    })
                }
        
        # Validar status si se está actualizando
        if 'status' in update_data:
            valid_statuses = ['OPEN', 'IN_PROGRESS', 'CLOSED']
            if update_data['status'] not in valid_statuses:
                return {
                    'statusCode': 400,
                    'headers': headers,
                    'body': json.dumps({
                        'error': f'Status inválido. Debe ser uno de: {", ".join(valid_statuses)}'
                    })
                }
        
        # Construir expresión de actualización
        allowed_fields = ['title', 'description', 'status', 'reporterId']
        update_expression = "SET updatedAt = :updatedAt"
        expression_values = {':updatedAt': datetime.utcnow().isoformat() + 'Z'}
        expression_names = {}
        
        # Agregar campos a actualizar
        for field in allowed_fields:
            if field in update_data:
                update_expression += f", #{field} = :{field}"
                expression_names[f'#{field}'] = field
                expression_values[f':{field}'] = update_data[field]
        
        if len(expression_values) == 1:  # Solo updatedAt
            return {
                'statusCode': 400,
                'headers': headers,
                'body': json.dumps({
                    'error': 'No se proporcionaron campos válidos para actualizar',
                    'allowedFields': allowed_fields
                })
            }
        
        # Actualizar el ticket
        response = table.update_item(
            Key={'id': ticket_id},
            UpdateExpression=update_expression,
            ExpressionAttributeNames=expression_names,
            ExpressionAttributeValues=expression_values,
            ReturnValues='ALL_NEW'
        )
        
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({
                'message': 'Ticket actualizado exitosamente',
                'ticket': response['Attributes']
            })
        }
        
    except json.JSONDecodeError:
        return {
            'statusCode': 400,
            'headers': headers,
            'body': json.dumps({'error': 'JSON inválido en el body'})
        }
    except ClientError as e:
        print(f"Error DynamoDB en update_ticket: {e}")
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({'error': 'Error al actualizar en la base de datos'})
        }
    except Exception as e:
        print(f"Error en update_ticket: {e}")
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({'error': 'Error al actualizar el ticket'})
        }

def delete_ticket(ticket_id, headers):
    """
    Eliminar un ticket
    DELETE /v1/tickets/{id}
    """
    try:
        if not ticket_id:
            return {
                'statusCode': 400,
                'headers': headers,
                'body': json.dumps({'error': 'ID del ticket es requerido'})
            }
        
        # Verificar que el ticket existe
        existing_ticket = table.get_item(Key={'id': ticket_id})
        if 'Item' not in existing_ticket:
            return {
                'statusCode': 404,
                'headers': headers,
                'body': json.dumps({
                    'error': 'Ticket no encontrado',
                    'id': ticket_id
                })
            }
        
        # Eliminar el ticket
        table.delete_item(Key={'id': ticket_id})
        
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({
                'message': 'Ticket eliminado exitosamente',
                'id': ticket_id
            })
        }
        
    except ClientError as e:
        print(f"Error DynamoDB en delete_ticket: {e}")
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({'error': 'Error al eliminar de la base de datos'})
        }
    except Exception as e:
        print(f"Error en delete_ticket: {e}")
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({'error': 'Error al eliminar el ticket'})
        }

# Funciones adicionales útiles

def get_tickets_by_status(status, headers):
    """
    Función adicional: Obtener tickets por status
    (Requiere un GSI en la tabla con status como clave)
    """
    try:
        valid_statuses = ['OPEN', 'IN_PROGRESS', 'CLOSED']
        if status not in valid_statuses:
            return {
                'statusCode': 400,
                'headers': headers,
                'body': json.dumps({
                    'error': f'Status inválido. Debe ser uno de: {", ".join(valid_statuses)}'
                })
            }
        
        # Usar scan con filter por ahora (para GSI usarías query)
        response = table.scan(
            FilterExpression='#status = :status',
            ExpressionAttributeNames={'#status': 'status'},
            ExpressionAttributeValues={':status': status}
        )
        
        tickets = response['Items']
        
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({
                'tickets': tickets,
                'count': len(tickets),
                'status': status
            })
        }
        
    except Exception as e:
        print(f"Error en get_tickets_by_status: {e}")
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({'error': 'Error al obtener tickets por status'})
        }

def get_tickets_by_reporter(reporter_id, headers):
    """
    Función adicional: Obtener tickets por reporterId
    """
    try:
        response = table.scan(
            FilterExpression='reporterId = :reporterId',
            ExpressionAttributeValues={':reporterId': reporter_id}
        )
        
        tickets = response['Items']
        tickets.sort(key=lambda x: x.get('createdAt', ''), reverse=True)
        
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({
                'tickets': tickets,
                'count': len(tickets),
                'reporterId': reporter_id
            })
        }
        
    except Exception as e:
        print(f"Error en get_tickets_by_reporter: {e}")
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({'error': 'Error al obtener tickets por reporter'})
        }
