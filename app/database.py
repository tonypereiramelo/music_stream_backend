from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME", "music_db")

client = AsyncIOMotorClient(MONGO_URI)
database = client[DB_NAME]

# Coleções do banco
music_collection = database["music"]
user_collection = database["users"]  # Se houver autenticação

async def get_db():
    return database
