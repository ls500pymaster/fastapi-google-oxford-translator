from database.database import get_database
from models.word_model import WordModel


async def get_word_details(word: str):
	db = await get_database()
	collection = db[WordModel.Config.collection_name]
	word_data = await collection.find_one({"word": word})
	if word_data:
		return WordModel(**word_data)
	return None


async def add_word_details(word_data: dict):
	db = await get_database()
	collection = db[WordModel.Config.collection_name]
	await collection.insert_one(word_data)


async def list_words(skip: int, limit: int, filter_word: str = None):
	db = await get_database()
	collection = db[WordModel.Config.collection_name]
	query = {}
	if filter_word:
		query["word"] = {"$regex": filter_word, "$options": "i"}
	cursor = collection.find(query, skip=skip, limit=limit)
	words = []
	async for document in cursor:
		words.append(WordModel(**document))
	return words


async def delete_word(word: str):
	db = await get_database()
	collection = db[WordModel.Config.collection_name]
	result = await collection.delete_one({"word": word})
	return result.deleted_count > 0

