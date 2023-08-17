
from mangum import Mangum
from fastapi import FastAPI, APIRouter, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from routes import app_router
from datetime import datetime
from fastapi.staticfiles import StaticFiles
from pathlib import Path

###from starlette.websockets import WebSocket

app = FastAPI(
    title='test fast api',
    description='fast api',
    docs_url='/docs',
)

app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


router = APIRouter()

app.include_router(app_router.router)

handler = Mangum(app)