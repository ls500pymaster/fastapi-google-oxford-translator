from typing import List, Optional

from fastapi import APIRouter, HTTPException, Query

from crud.word_crud import get_word_details, add_word_details, list_words, delete_word
from schemas.word_schema import WordSchema
from services.google_translate_client import fetch_word_from_google

router = APIRouter()


@router.get("/words/{word}", response_model=WordSchema, summary="Get word details")
async def read_word(word: str):
    word_data = await get_word_details(word)
    if not word_data:
        word_data = await fetch_word_from_google(word)
        if not word_data:
            raise HTTPException(status_code=404, detail="Word not found")
        await add_word_details(word_data.dict())
    return word_data


@router.get("/words", response_model=List[WordSchema], summary="List words")
async def get_words(skip: int = 0,
                    limit: int = 10,
                    filter_word: Optional[str] = Query(None, description="Filter words by partial match")):
    words = await list_words(skip, limit, filter_word)
    return words


@router.delete("/words/{word}", summary="Delete a word")
async def delete_word_endpoint(word: str):
    success = await delete_word(word)
    if not success:
        raise HTTPException(status_code=404, detail="Word not found")
    return {"message": "Word deleted successfully"}
