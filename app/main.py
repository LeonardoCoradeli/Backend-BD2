# app/main.py
import databases
from fastapi import FastAPI
from app.api.v1 import UserController,CardController, DeckController
from app.core import config
from app.data.BaseRepository import BaseRepository

# Configuração da conexão com o banco de dados
database = databases.Database(config.DATABASE_URL)
BaseRepository.database = database  # Define o banco de dados padrão para o repositório
app = FastAPI()

# Configura eventos de startup e shutdown para conectar/desconectar do banco
@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# Inclui os routers definidos nos módulos de endpoints
app.include_router(UserController.router, prefix="/api/v1", tags=["users"])
app.include_router(CardController.router, prefix="/api/v1", tags=["cards"])
app.include_router(DeckController.router, prefix="/api/v1", tags=["decks"])
