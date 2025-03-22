from app.database import music_collection
from app.api.models.music import MusicInDB
from bson import ObjectId

# Function to insert a new music document into the database
async def insert_music(music: MusicInDB) -> MusicInDB:
    music_dict = music.dict(exclude_unset=True)  # Exclude unset fields from being sent to MongoDB
    result = await music_collection.insert_one(music_dict)  # Insert the document
    music.id = str(result.inserted_id)  # Set the id field to the MongoDB inserted_id
    return music  # Return the music with the id

# Example function to find music by its ID
async def get_music_by_id(music_id: str) -> MusicInDB:
    document = await music_collection.find_one({"_id": ObjectId(music_id)})
    if document:
        return MusicInDB(**document)  # Return the document as a MusicInDB model
    return None

# Example function to list all music
async def list_music() -> list:
    documents = await music_collection.find().to_list(length=100)  # Get up to 100 music documents
    return [MusicInDB(**doc) for doc in documents]
