from fastapi import APIRouter, HTTPException
from app.api.services.music_service import insert_music, get_music_by_id, list_music
from app.api.models.music import Music, MusicInDB

router = APIRouter()

# Route to add a new music
@router.post("/", response_model=MusicInDB)
async def add_music(music: Music):
    music_in_db = await insert_music(MusicInDB(**music.model_dump()))
    return music_in_db

# Route to get a music by ID
@router.get("/{music_id}", response_model=MusicInDB)
async def get_music(music_id: str):
    music = await get_music_by_id(music_id)
    if not music:
        raise HTTPException(status_code=404, detail="Music not found")
    return music

# Route to list all music
@router.get("/", response_model=list[MusicInDB])
async def get_all_music():
    music_list = await list_music()
    return music_list
