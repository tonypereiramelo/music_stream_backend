import asyncio
from app.database import database, music_collection

async def test_connection():
    try:
        # Verifica se consegue listar as coleções do banco
        collections = await database.list_collection_names()
        print(f"Conectado ao MongoDB! Coleções disponíveis: {collections}")

        # Teste de inserção e leitura
        test_doc = {"title": "Test Song", "artist": "Test Artist"}
        result = await music_collection.insert_one(test_doc)
        print(f"Documento inserido com ID: {result.inserted_id}")

        # Verifica se a inserção funcionou
        found_doc = await music_collection.find_one({"_id": result.inserted_id})
        print("Documento encontrado no banco:", found_doc)

        # Limpeza: remover o documento de teste
        await music_collection.delete_one({"_id": result.inserted_id})
        print("Teste concluído e documento removido.")

    except Exception as e:
        print(f"Erro ao conectar ao MongoDB: {e}")

# Rodar o teste
asyncio.run(test_connection())
