import unittest

from src.mapper.string_to_word_mapper import StringToWordMapper
from src.service.syllable_service import SyllableService


class SyllableServiceTest(unittest.TestCase):
    """Unit tests for the SyllableService class"""

    def setUp(self):
        """Set up the test case by initializing required objects."""
        self.test_words = self.__get_test_words()
        self.syllable_service = SyllableService()
        self.string_to_word_mapper = StringToWordMapper()

    def test_get_divided_word_by_syllables(self):
        """Test the divide_word_by_syllables method of SyllableService."""
        for word_str in self.test_words:
            word = self.string_to_word_mapper.map_to_word(word_str=word_str)
            divided_by_syllables = self.syllable_service.divide_word_by_syllables(
                word=word
            )
            expected = self.test_words[word_str].upper()
            self.assertEqual(expected, divided_by_syllables)

    @classmethod
    def __get_test_words(cls) -> dict:
        """Get a dictionary of test words and their expected syllable divisions.

        Returns:
            dict: A dictionary where the keys are the test words and the values are their expected syllable divisions.
        """
        return {
            "суштество": "суш-тес-тво",
            "загатка": "за-гат-ка",
            "производител": "про-из-во-ди-тел",
            "сигнификантност": "сиг-ни-фи-кант-ност",
            "аурора": "а-у-ро-ра",
            "авионски": "а-ви-онс-ки",
            "антропологија": "ант-ро-по-ло-ги-ја",
            "смртта": "смрт-та",
            "оздравениот": "оз-дра-ве-ни-от",
            "крвав": "кр-вав",
            "крвавиот": "кр-ва-ви-от",
            "здравствен": "здравс-твен",
            "исклучителност": "ис-клу-чи-тел-ност",
            "претчувство": "прет-чувс-тво",
            "идеално": "и-де-ал-но",
            "иако": "и-а-ко",
            "`ржен": "`р-жен",
            "срмата": "ср-ма-та",
            "антрополог": "ант-ро-по-лог",
            "апарат": "а-па-рат",
            "противавионски": "про-ти-ва-ви-онс-ки",
            "превешто": "пре-веш-то",
            "најсушто": "нај-суш-то",
            "распиштолувањава": "рас-пиш-то-лу-ва-ња-ва",
            "приштосувањана": "приш-то-су-ва-ња-на",
            "поопштословенска": "по-оп-штос-ло-венс-ка",
            "ништожество": "ниш-то-жес-тво"
        }
