import boto3

def listar(event, context):
    # Entrada (json)
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('compras')
    response = table.scan() # Lee todos los registros
    items = response['Items']
    num_reg = response['Count']
    # Salida (json)
    return {
        'statusCode': 200,
        'num_reg': num_reg,
        'compras': items
    }
def buscar(event, context):
    # Entrada (json)
    compra_id = event['body']['compra_id']
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('compras')
    response = table.query(
        KeyConditionExpression=Key('compra_id').eq(compra_id)
    )
    items = response['Items']
    # Salida (json)
    return {
        'statusCode': 200,
        'response': items
    }

def crear(event, context):
    # Entrada (json)
    compra = event['body']
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('compras')
    response = table.put_item(Item=compra)
    # Salida (json)
    return {
        'statusCode': 200,
        'response': response
    }
def modificar(event, context):
    # Entrada (json)
    compra_id = event['body']['compra_id']
    datos = event['body']['datos']
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('compras')
    response = table.update_item(
        Key={
            'compra_id': compra_id
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
    compra_id = event['body']['compra_id']    
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('compras')
    response = table.delete_item(
        Key={
            'compra_id': compra_id
        }
    )
    # Salida (json)
    return {
        'statusCode': 200,
        'response': response
    }