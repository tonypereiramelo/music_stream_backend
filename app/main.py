from fastapi import FastAPI
from app.api.routes.music_route import router as music_router  # Importando as rotas de música

app = FastAPI()

# Incluindo as rotas de música na aplicação
app.include_router(music_router, prefix="/music", tags=["music"])
