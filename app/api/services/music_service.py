from app.database import music_collection
from app.api.models.music import MusicInDB
from bson import ObjectId

# Function to insert a new music document into the database
async def insert_music(music: MusicInDB) -> MusicInDB:
    music_dict = music.model_dump(exclude_unset=True)  # Exclude unset fields from being sent to MongoDB
    result = await music_collection.insert_one(music_dict)  # Insert the document
    music.id = str(result.inserted_id)  # Set the id field to the MongoDB inserted_id
    return music  # Return the music with the id

# Example function to find music by its ID
async def get_music_by_id(music_id: str) -> MusicInDB:
    document = await music_collection.find_one({"_id": ObjectId(music_id)})
    if document:
        return MusicInDB(**document)  # Return the document as a MusicInDB model
    return None

# Function to update a song
async def update_music(music_id: str, music: MusicInDB) -> MusicInDB:
    updated_data = music.dict(exclude_unset=True)
    result = await music_collection.update_one(
        {"_id": ObjectId(music_id)}, {"$set": updated_data}
    )
    if result.matched_count:
        return await get_music_by_id(music_id)  # Return updated music
    return None

# Function to delete a song
async def delete_music(music_id: str) -> dict:
    result = await music_collection.delete_one({"_id": ObjectId(music_id)})
    if result.deleted_count:
        return {"message": "Music deleted successfully"}
    return None

# Example function to list all music
async def list_music() -> list:
    documents = await music_collection.find().to_list(length=100)  # Get up to 100 music documents
    return [MusicInDB(**doc) for doc in documents]

# Function to find music by title
async def find_music_by_title(title: str) -> list:
    documents = await music_collection.find({"title": {"$regex": title, "$options": "i"}}).to_list(length=100)
    return [MusicInDB(**doc) for doc in documents]

# Function to find music by artist/band name
async def find_music_by_artist(artist: str) -> list:
    documents = await music_collection.find({"artist": {"$regex": artist, "$options": "i"}}).to_list(length=100)
    return [MusicInDB(**doc) for doc in documents]

# Function to find music by album (if added to the model)
async def find_music_by_album(album: str) -> list:
    documents = await music_collection.find({"album": {"$regex": album, "$options": "i"}}).to_list(length=100)
    return [MusicInDB(**doc) for doc in documents]
