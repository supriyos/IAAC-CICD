import boto3
import json
import os
import time
from services.chatgpt_service import ChatGpt

chatgpt_object = ChatGpt()

class ApiGatewayWebSocketHelper:
    def __init__(self) -> None:
        # self.websocket_client = boto3.client('apigatewaymanagementapi', endpoint_url='https://bms5spxaid.execute-api.eu-west-2.amazonaws.com/production')
        self.websocket_client = boto3.client('apigatewaymanagementapi', endpoint_url='https://bms5spxaid.execute-api.eu-west-2.amazonaws.com/prods')        
    def put_message_in_socket(self,message, connection_id:str):
        self.websocket_client.post_to_connection(ConnectionId=connection_id,Data=json.dumps(message).encode("utf-8"))

def handler(event, context):
    websocket = ApiGatewayWebSocketHelper()
    print('######### the event is =',event)
    if event['requestContext']['routeKey'] == "$connect":
        return{
            'statusCode': 200,
            'body': 'Socket Connected'
        }
    elif event['requestContext']['routeKey'] == "$disconnect":
        return{
            'statusCode': 200,
            'body': 'Socket Disconnected'
        }
    elif event['requestContext']['routeKey'] == "sendMessage":
        try:
            print('########## Entered message block of stack7 lambda')
            print( json.loads(event['body'])['message'] )
            user_message = json.loads(event['body'])['message']

            chat_gpt_reply = chatgpt_object.chatgpt_service(user_message)
            print('#### gpt reply = ',chat_gpt_reply)
            
            connection_id = event['requestContext']['connectionId']
            
            websocket.put_message_in_socket(chat_gpt_reply,connection_id)
            return{
                'statusCode': 200,
                'body': 'message sent'
            }            
        except Exception as e:
            return {
                'statusCode': 400
            }
    elif event['requestContext']['routeKey'] == "$default":
        try:
            print('########## Entered default block ')            
            connection_id = event['requestContext']['connectionId']       
            websocket.put_message_in_socket("HELLO FROM default LAMBDA2",connection_id)

            return{
                'statusCode': 200,
                'body': 'message sent'
            }            
        except Exception as e:
            return {
                'statusCode': 400
            }            
