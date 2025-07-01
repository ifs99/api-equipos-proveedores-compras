import boto3

def listar(event, context):
    # Entrada (json)
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('equipos')
    response = table.scan() # Lee todos los registros
    items = response['Items']
    num_reg = response['Count']
    # Salida (json)
    return {
        'statusCode': 200,
        'num_reg': num_reg,
        'equipos': items
    }
def buscar(event, context):
    # Entrada (json)
    equipo_id = event['body']['equipo_id']
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('equipos')
    response = table.query(
        KeyConditionExpression=Key('equipo_id').eq(equipo_id)
    )
    items = response['Items']
    # Salida (json)
    return {
        'statusCode': 200,
        'response': items
    }

def crear(event, context):
    # Entrada (json)
    equipo = event['body']
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('equipos')
    response = table.put_item(Item=equipo)
    # Salida (json)
    return {
        'statusCode': 200,
        'response': response
    }
def modificar(event, context):
    # Entrada (json)
    equipo_id = event['body']['equipo_id']
    datos = event['body']['datos']
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('equipos')
    response = table.update_item(
        Key={
            'equipo_id': equipo_id
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
    equipo_id = event['body']['equipo_id']    
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('equipos')
    response = table.delete_item(
        Key={
            'equipo_id': equipo_id
        }
    )
    # Salida (json)
    return {
        'statusCode': 200,
        'response': response
    }