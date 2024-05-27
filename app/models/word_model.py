from pydantic import BaseModel, Field
from typing import List


class WordModel(BaseModel):
	word: str = Field(...)
	definitions: List[str] = Field(...)
	synonyms: List[str] = Field(...)
	translations: List[str] = Field(...)
	examples: List[str] = Field(...)

	class Config:
		collection_name = "words"
