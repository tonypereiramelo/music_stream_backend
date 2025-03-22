from fastapi import APIRouter, HTTPException
from app.api.services.music_service import (
    insert_music, get_music_by_id, list_music,
    find_music_by_title, find_music_by_artist, find_music_by_album
)
from app.api.models.music import Music, MusicInDB

router = APIRouter()

@router.post("/", response_model=MusicInDB)
async def add_music(music: Music):
    music_in_db = await insert_music(MusicInDB(**music.model_dump()))
    return music_in_db

@router.get("/{music_id}", response_model=MusicInDB)
async def get_music(music_id: str):
    music = await get_music_by_id(music_id)
    if not music:
        raise HTTPException(status_code=404, detail="Music not found")
    return music

@router.get("/", response_model=list[MusicInDB])
async def get_all_music():
    music_list = await list_music()
    return music_list

@router.get("/search/title/{title}", response_model=list[MusicInDB])
async def search_music_by_title(title: str):
    music_list = await find_music_by_title(title)
    return music_list

@router.get("/search/artist/{artist}", response_model=list[MusicInDB])
async def search_music_by_artist(artist: str):
    music_list = await find_music_by_artist(artist)
    return music_list

@router.get("/search/album/{album}", response_model=list[MusicInDB])
async def search_music_by_album(album: str):
    music_list = await find_music_by_album(album)
    return music_list
