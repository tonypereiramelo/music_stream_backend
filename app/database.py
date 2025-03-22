from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME", "music_db")

# Create a client to connect to MongoDB
client = AsyncIOMotorClient(MONGO_URI)
database = client[DB_NAME]

# Collections in the database
music_collection = database["music"]
user_collection = database["users"]  # If authentication is required

# Function to get the database instance
async def get_db():
    return database
