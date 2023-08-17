# standard imports
import json
import sys
import os

# external imports
import openai
#from IPython.display import Image, display

# local imports
# cur_dir = "G:/My Drive/projects/ai_iac/"
# os.chdir(cur_dir)
from models.constants_model import Constants

constants = Constants()
openai.api_key = constants.OPENAPI_KEY

class ChatGpt:
    def __init__(self):
        # configurations
        self.messages = constants.OPENAPI_SET_CONTEXT_MESSAGE
        self.custom_data_configs = str(constants.CUSTOM_DATA_CONFIGS)
        self.template_found = None

        self.LAMBDA_S3_BUCKET = constants.LAMBDA_S3_BUCKET
        self.AWS_REGION = constants.AWS_REGION     
        # self.BASE_PATH = cur_dir

        self.messages.append({'role':'user','content':self.custom_data_configs})

    def chatgpt_service(self, user_message):
        if user_message:
            template_found = None
            self.messages.append({'role':'user','content':user_message})
            chat = openai.ChatCompletion.create(model='gpt-3.5-turbo',messages=self.messages)
            reply = chat.choices[0].message.content
            self.messages.append({'role':'assistant','content':reply})

            return reply
