from my_lambda.log import log
import json

def lambda_handler(event, context):   
    log(f"Log de execução do evento após o GitHub Actions: {json.dumps(event)} ") 
    return {
        'statusCode': 200,
        'body': f"<html><body>Dados da Requisicao: {json.dumps(event)}</body></html>",
        'headers': {
            "content-type": "text/html"
        }
    }
