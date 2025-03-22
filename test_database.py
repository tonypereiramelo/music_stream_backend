import asyncio
from app.api.database import database, music_collection

async def test_connection():
    try:
        # Check if it is possible to list the collections in the database
        collections = await database.list_collection_names()
        print(f"Connected to MongoDB! Available collections: {collections}")

        # Test insertion and retrieval
        test_doc = {"title": "Test Song", "artist": "Test Artist"}
        result = await music_collection.insert_one(test_doc)
        print(f"Document inserted with ID: {result.inserted_id}")

        # Check if the insertion worked
        found_doc = await music_collection.find_one({"_id": result.inserted_id})
        print("Document found in the database:", found_doc)

        # Cleanup: remove the test document
        await music_collection.delete_one({"_id": result.inserted_id})
        print("Test completed and document removed.")

    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")

# Run the test
asyncio.run(test_connection())
