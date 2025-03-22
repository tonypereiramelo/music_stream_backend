from pydantic import BaseModel, Field
from typing import Optional

# Pydantic model for Music data validation
class Music(BaseModel):
    title: str = Field(..., example="Song Title")  # Title of the song
    artist: str = Field(..., example="Artist Name")  # Artist of the song
    genre: Optional[str] = Field(None, example="Pop")  # Genre of the song (optional)
    audio_url: str = Field(..., example="http://example.com/audio.mp3")  # URL for the audio file
    duration: Optional[int] = Field(None, example=180)  # Duration in seconds (optional)

    class Config:
        # Allow population of models from MongoDB data (fields like _id)
        orm_mode = True

# MongoDB model to work with the database
class MusicInDB(Music):
    id: str = Field(..., alias="_id")  # _id from MongoDB, we alias it to id for Pydantic
