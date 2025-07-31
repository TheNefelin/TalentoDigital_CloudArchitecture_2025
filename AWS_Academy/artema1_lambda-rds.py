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