from src.domain.phoneme import Phoneme
from src.domain.phonetic_element import PhoneticElement
from src.domain.word import Word


class StringToWordMapper:
    """
    Mapper class for converting a string to a Word object.

    """

    @classmethod
    def map_to_word(cls, word_str: str) -> Word:
        """
        Maps a string to a Word object.

        Args:
            word_str (str): The input string to be mapped.

        Returns:
            Word: The mapped Word object.

        Raises:
            KeyError: If a phoneme in the string is not found in the Phoneme enumeration.
        """
        word_str = word_str.upper()
        phonetic_elements: list[PhoneticElement] = [PhoneticElement(Phoneme.FC)]

        for raw_character in word_str:
            phoneme = Phoneme.__getitem__(raw_character)
            phonetic_element = PhoneticElement(phoneme=phoneme)

            if phonetic_element.is_vowel():
                previous_phonetic_element = phonetic_elements[-1]
                if previous_phonetic_element.is_vowel():
                    phonetic_elements.append(PhoneticElement(Phoneme.FC))

            phonetic_elements.append(phonetic_element)

        phonetic_elements.append(PhoneticElement(Phoneme.FC))

        return Word(phonetic_elements=phonetic_elements)
