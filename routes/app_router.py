from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import ORJSONResponse
from models.constants_model import Constants
from models.requests_model import GetTempRequest
from fastapi.templating import Jinja2Templates
from pathlib import Path
from fastapi.responses import HTMLResponse

#from services.sensor import SensorService

print('############## ENtered Router ###############')
print('##### static file path = ', Path(__file__))
print('##### static file path = ', Path(__file__).parent)
print('##### static file path = ', Path(__file__).parent.absolute())


#logger = Logger(service='app_router',level='INFO')
constants = Constants()
router = APIRouter()

# sophesticated html rendering
BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(BASE_PATH / 'templates')

@router.get('/get-temperature')
def root(request:Request) -> dict:
    """
        root
    """
    print('########### entered root method')
    return TEMPLATES.TemplateResponse(
        'index.html',
        {'request':request}
    )

#'sensors':[{'sensor_id':123},{'sensor_id':456}]
# @router.get('/')
# async def root():
#     return HTMLResponse(str(BASE_PATH) + '\templates\index.html')

@router.get('/get-temperature2')
def get_sensor_temperature():
    """
    Args:
    Returns:
    """
    print('############# Entered method ')
    return 'hello from sensor'