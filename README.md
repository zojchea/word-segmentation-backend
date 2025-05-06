# Graduation Thesis Project - Backend

This API provides endpoints for dividing words by syllables and morphemes. It utilizes the FastAPI framework and Python.

## Setup

1. Start the docker server:

   ```bash
   docker-compose up -d

2. Or run it locally:
   ```bash
   pip install -r requirements.txt
   python main.py

The API can be tested at http://localhost:8000/docs.

## API Endpoints

### GET /divide/syllables

- Divides a word by syllables.

- Request Parameters
   - word (str): The word to be divided. Only Cyrillic characters and the special character \` (Unicode range [\u0400-\u04FF`]) are allowed.
- Example Request
  ```bash
   GET /divide/syllables?word=суштество
- Example Response
  ```json
  {
      "wordBySyllables": "суш-тес-тво"
  }
  
### GET /divide/morphemes

- Divides a word by morphemes.

- Request Parameters
   - word (str): The word to be divided. Only Cyrillic characters and the special character \` (Unicode range [\u0400-\u04FF`]) are allowed.
- Example Request
  ```bash
   GET /divide/morphemes?word=суштество
- Example Response
  ```json
  {
      "wordByMorphemes": "суште-ство"
  }
