from motor.motor_asyncio import AsyncIOMotorClient

client = None


async def connect_to_mongo():
    global client
    client = AsyncIOMotorClient('mongodb://mongo:27017')
    print("Connected to MongoDB")


async def close_mongo_connection():
    client.close()
    print("Closed MongoDB connection")


async def get_database():
    return client.fastapi_translation_service
