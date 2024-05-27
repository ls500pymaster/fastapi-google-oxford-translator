from fastapi import FastAPI
from routers import word_router
from database.database import connect_to_mongo, close_mongo_connection
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="FastAPI Translation Service",
    description="API for translating words and fetching their details using Google Translate",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)


@app.on_event("startup")
async def startup_db_client():
    await connect_to_mongo()


@app.on_event("shutdown")
async def shutdown_db_client():
    await close_mongo_connection()

app.include_router(word_router.router, prefix="/api/v1")
