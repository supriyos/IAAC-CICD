from aws_lambda_powertools import Logger

logger = Logger(service='sensor',level='INFO')

class Constants:
    REGION = 'eu-west-2'
    OPENAPI_KEY = ''
    OPENAPI_SET_CONTEXT_MESSAGE = [{'role':'system', 'content':'you are a kind helpful assistant'}]

    CUSTOM_DATA_CONFIGS = 'CodeUri = "functions", Handler = "lambda_function.lambda_handler", "Runtime"= "python 3.10", "Path"= "/get_message"'
    LAMBDA_S3_BUCKET = ''
    AWS_REGION = ''


