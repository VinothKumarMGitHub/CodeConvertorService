import json
from xmlConvertor import ConvertToXML 
from readJson import paserJsonString
# import requests


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    try:
        pythonObj = paserJsonString( event["body"] )
        xmlString = ConvertToXML( pythonObj)

    except Exception as e:
        # Send some context about this error to Lambda Logs
        raise e

    return {
        "statusCode": 200,
         "headers":{
             'Access-Control-Allow-Origin':"*",
             "Content-Type": "application/json"
         },
        "body": json.dumps({
            "message": str(xmlString),
            # "location": ip.text.replace("\n", "")
        }),
    }
