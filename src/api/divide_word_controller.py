from fastapi import APIRouter
from pydantic import constr

from src.mapper.string_to_word_mapper import StringToWordMapper
from src.repository.word_repository import WordRepository
from src.service.morpheme_service import MorphemeService
from src.service.syllable_service import SyllableService


class DivideWordController:
    """Controller for dividing words by syllables and morphemes."""
    def __init__(self):
        """Initialize the controller by setting up the required services and dependencies."""
        self.router = APIRouter()
        self.syllable_service = SyllableService()
        word_repository = WordRepository()
        self.morpheme_service = MorphemeService(word_repository=word_repository)

        @self.router.get("/healthcheck")
        def healthcheck() -> dict[str, bool]:
            return {"healthy": True}

        @self.router.get("/divide/syllables")
        def divide_by_syllables(text: constr(regex="[\u0400-\u04FF`]+")) -> str:
            """Endpoint for dividing text by syllables.

            Args:
                text (str): The text to be divided.

            Returns:
                str: Divided text by syllables.
            """
            words_array = text.split()
            response_text = ""
            for word in words_array:
                word_by_syllables = self.syllable_service.divide_word_by_syllables(
                    word=StringToWordMapper.map_to_word(word_str=word)
                )
                response_text = response_text + " " + word_by_syllables

            return response_text

        @self.router.get("/divide/morphemes")
        def divide_by_morphemes(word: constr(regex="[\u0400-\u04FF]+")) -> str:
            """Endpoint for dividing word by morphemes.

            Args:
                word (str): The word to be divided.

            Returns:
                str: Divided word by morphemes.
            """
            return self.morpheme_service.divide_word_by_morphemes(word=word)


