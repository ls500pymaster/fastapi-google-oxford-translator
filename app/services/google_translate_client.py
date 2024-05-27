import logging
import os

import requests
from deep_translator import GoogleTranslator
from dotenv import load_dotenv

from models.word_model import WordModel

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

OXFORD_APP_ID = os.getenv("OXFORD_APP_ID")
OXFORD_APP_KEY = os.getenv("OXFORD_APP_KEY")
OXFORD_BASE_URL = os.getenv("OXFORD_BASE_URL")


async def fetch_word_from_oxford(word: str):
    if not OXFORD_BASE_URL:
        logger.error("OXFORD_BASE_URL is not set.")
        return None

    url = f"{OXFORD_BASE_URL}/entries/en-gb/{word.lower()}"
    headers = {
        "app_id": OXFORD_APP_ID,
        "app_key": OXFORD_APP_KEY
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        logger.error(f"Failed to fetch data from Oxford API for word '{word}'. Status code: {response.status_code}")
        return None
    return response.json()


async def fetch_word_from_google(word: str):
	try:
		translator = GoogleTranslator(source='en', target='en')
		translation = translator.translate(word)
	except Exception as e:
		print(f"Translation error: {e}")
		return None

	oxford_data = await fetch_word_from_oxford(word)
	if not oxford_data:
		logger.error(f"No data found for word '{word}' in Oxford API.")
		return None

	definitions = []
	synonyms = []
	examples = []

	try:
		lexical_entries = oxford_data["results"][0]["lexicalEntries"]
		for lexical_entry in lexical_entries:
			for entry in lexical_entry["entries"]:
				for sense in entry["senses"]:
					if "definitions" in sense:
						definitions.extend(sense["definitions"])
					if "examples" in sense:
						examples.extend([ex["text"] for ex in sense["examples"]])
					if "synonyms" in sense:
						synonyms.extend([syn["text"] for syn in sense["synonyms"]])
	except Exception as e:
		logger.error(f"Error extracting data from Oxford API response: {e}")
		return None

	translations = [translation]

	word_data = WordModel(
		word=word,
		definitions=definitions,
		synonyms=synonyms,
		translations=translations,
		examples=examples
	)

	return word_data