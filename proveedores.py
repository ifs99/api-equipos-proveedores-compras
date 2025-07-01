import boto3
from boto3.dynamodb.conditions import Key

def listar(event, context):
    # Entrada (json)
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('proveedores')
    response = table.scan() # Lee todos los registros
    items = response['Items']
    num_reg = response['Count']
    # Salida (json)
    return {
        'statusCode': 200,
        'num_reg': num_reg,
        'proveedores': items
    }
def buscar(event, context):
    # Entrada (json)
    proveedor_id = event['body']['proveedor_id']
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('proveedores')
    response = table.query(
        KeyConditionExpression=Key('proveedor_id').eq(proveedor_id)
    )
    items = response['Items']
    # Salida (json)
    return {
        'statusCode': 200,
        'response': items
    }

def crear(event, context):
    # Entrada (json)
    proveedor = event['body']
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('proveedores')
    response = table.put_item(Item=proveedor)
    # Salida (json)
    return {
        'statusCode': 200,
        'response': response
    }
def modificar(event, context):
    # Entrada (json)
    proveedor_id = event['body']['proveedor_id']
    datos = event['body']['datos']
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('proveedores')
    response = table.update_item(
        Key={
            'proveedor_id': proveedor_id
        },
        UpdateExpression="set datos=:datos_a_actualizar",
        ExpressionAttributeValues={
            ':datos_a_actualizar': datos
        },
        ReturnValues="UPDATED_NEW"
    )
    # Salida (json)
    return {
        'statusCode': 200,
        'response': response
    }

def eliminar(event, context):
    # Entrada (json)
    proveedor_id = event['body']['proveedor_id']    
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('proveedores')
    response = table.delete_item(
        Key={
            'proveedor_id': proveedor_id
        }
    )
    # Salida (json)
    return {
        'statusCode': 200,
        'response': response
    }
