# FastAPI Translation Service

## Overview

The FastAPI Translation Service is a microservice that provides a JSON API for word definitions, synonyms, translations, and examples using the Oxford Dictionaries API and Google Translate. This service supports fetching detailed word information and caching it in a MongoDB database.

## Features

- **Get Word Details**: Fetches definitions, synonyms, translations, and examples for a given word.
- **List Stored Words**: Retrieves a list of words stored in the database with pagination, sorting, and filtering.
- **Delete Word**: Removes a word from the database.

## Endpoints

1. **Get Word Details**:
   - URL: `/api/v1/words/{word}`
   - Method: `GET`
   - Description: Fetches and returns the details of the given word. If the word is not found in the database, it fetches the details from the Oxford API and Google Translate, stores it in the database, and returns the details.

2. **List Stored Words**:
   - URL: `/api/v1/words`
   - Method: `GET`
   - Description: Returns a list of words stored in the database with pagination, sorting, and filtering by word.

3. **Delete Word**:
   - URL: `/api/v1/words/{word}`
   - Method: `DELETE`
   - Description: Deletes the specified word from the database.

## Project Structure
```
fastapi_translation_service/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── word_model.py
│   ├── routers/
│   │   ├── __init__.py
│   │   └── word_router.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── word_schema.py
│   ├── crud/
│   │   ├── __init__.py
│   │   └── word_crud.py
│   ├── database/
│   │   ├── __init__.py
│   │   └── database.py
│   └── services/
│       ├── __init__.py
│       └── google_translate_client.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```


## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Setup
1. **Clone the Repository**:

   ```bash
   git clone git@github.com:ls500pymaster/fastapi-google-translator.git
   cd fastapi-google-translator
   
2. **Create .env File:**

OXFORD_APP_ID=your_oxford_app_id

OXFORD_APP_KEY=your_oxford_app_key

OXFORD_BASE_URL=https://od-api.oxforddictionaries.com/api/v2

3. **Register Oxford Dictionaries Account**

- https://developer.oxforddictionaries.com/admin/applications/
- Create application and prepare API Base URL, Application ID, Application Key


4. **Build and Run the Docker Containers:**

   ```bash
   docker-compose up --build```

### Usage
**Access the API Documentation:**

- Once the application is running, you can access the Swagger UI for API documentation at: http://localhost:8000/docs
- Alternatively, you can use ReDoc at: http://localhost:8000/redoc
- Example CURL request to get word details:

```bash curl -X 'GET' 'http://127.0.0.1:8000/api/v1/words/ace' -H 'accept: application/json```






