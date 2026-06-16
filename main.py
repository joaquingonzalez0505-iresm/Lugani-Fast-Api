from fastapi import FastAPI
from app.api.v1.api import api_router

app = FastAPI()

# Incluye todas las rutas de la versión 1 bajo el prefijo general api/v1
app.include_router(api_router, prefix="/api/v1")