from src.domain.word import Word


class SyllableService:
    """
    The SyllableService class encapsulates the core algorithm for syllable segmentation
    of Macedonian words. It provides a method to divide a given word into syllables based
    on phonetic attributes and triplet differences amongst its phonetic elements.

    Methods:
        - divide_word_by_syllables(word: Word) -> str:
            Divides a word into syllables based on the phonetic attributes of its letters.
        - __find_syllable_border_index(word: Word, index: int, phoneme_sonorities: list[int]) -> int | None:
            Recursively finds the index of the syllable border within a word based on phoneme sonorities.
        - __get_strictly_decline_break_index(phoneme_sonorities: list[int]) -> int | None:
            Finds the index where the phoneme sonorities strictly decline breaks within a list.

    Usage:
        syllable_service = SyllableService()
        segmented_word = syllable_service.divide_word_by_syllables(word)
    """

    def divide_word_by_syllables(self, word: Word) -> str:
        """
        Divides a word into syllables.

        Args:
            word (Word): The Word object representing the word to be divided.

        Returns:
            str: The divided word represented as a string.

        """
        phonetic_elements = word.phonetic_elements
        word_by_syllables = ""
        index = 1
        while index < len(phonetic_elements) - 1:
            phonetic_element = phonetic_elements[index]

            if phonetic_element.is_special_character():
                if phonetic_element.phoneme == "`":
                    word_by_syllables += phonetic_element.phoneme
                index += 1
                continue

            word_by_syllables += phonetic_element.phoneme
            if (phonetic_element.triplet_difference > 0 or (phonetic_element.triplet_difference == 0 and phonetic_element.phoneme_sonority >= 5)) and index < len(phonetic_elements) - 2:
                next_phonetic_element = word.get_next_phonetic_element(current_index=index)
                if index + 2 <= len(phonetic_elements) - 2:
                    after_next_phonetic_element = word.get_next_phonetic_element(
                        current_index=index + 1)

                    if next_phonetic_element.triplet_difference < -10 and after_next_phonetic_element.triplet_difference > 0 and (
                            index != 1 or phonetic_element.is_vowel()):
                        word_by_syllables += "-"
                    elif next_phonetic_element.triplet_difference < 0 and after_next_phonetic_element.triplet_difference < 0:
                        syllable_border_index = self.__find_syllable_border_index(
                            word=word,
                            index=index + 3,
                            phoneme_sonorities=[next_phonetic_element.phoneme_sonority, after_next_phonetic_element.phoneme_sonority]
                        )

                        if syllable_border_index is not None:
                            count_index = index + 1
                            while count_index <= syllable_border_index:
                                word_by_syllables += phonetic_elements[count_index].phoneme
                                count_index += 1
                            word_by_syllables += "-"
                            index = count_index
                            continue
                        else:
                            if index + 3 == len(phonetic_elements) - 1:
                                word_by_syllables += next_phonetic_element.phoneme
                                word_by_syllables += after_next_phonetic_element.phoneme
                            else:
                                word_by_syllables += next_phonetic_element.phoneme
                                word_by_syllables += "-"
                                word_by_syllables += after_next_phonetic_element.phoneme

                            index += 3
                            continue
                else:
                    word_by_syllables += next_phonetic_element.phoneme
                    return word_by_syllables
            index += 1
        return word_by_syllables

    def __find_syllable_border_index(
            self,
            word: Word,
            index: int,
            phoneme_sonorities: list[int]
    ) -> int | None:
        """
        Recursively finds the index of the syllable border within a word.

        Args:
            word (Word): The Word object representing the word being analyzed.
            index (int): The starting index for the search.
            phoneme_sonorities (list[int]): List of phoneme sonorities for comparison.

        Returns:
            int | None: The index of the syllable border, or None if not found.

        """
        if index < len(word.phonetic_elements) - 2 and word.phonetic_elements[index]:
            phonetic_element = word.phonetic_elements[index]
            if phonetic_element.triplet_difference < 0:
                phoneme_sonorities.append(phonetic_element.phoneme_sonority)
                strictly_decline_break_index = self.__get_strictly_decline_break_index(
                    phoneme_sonorities=phoneme_sonorities
                )
                if strictly_decline_break_index is not None:
                    return index - (len(phoneme_sonorities) - strictly_decline_break_index - 1)
                else:
                    return self.__find_syllable_border_index(
                        word=word, index=index + 1, phoneme_sonorities=phoneme_sonorities)

    @classmethod
    def __get_strictly_decline_break_index(
            cls,
            phoneme_sonorities: list[int]
    ) -> int | None:
        """
        Finds the index where the phoneme sonorities strictly decline breaks within a list.

        Args:
            phoneme_sonorities (list[int]): List of phoneme sonorities.

        Returns:
            int | None: The index of the phoneme where the break happens,
                        or None if there is no break in the strictly declining.

        """
        for index in range(0, len(phoneme_sonorities) - 1):
            if phoneme_sonorities[index + 1] >= phoneme_sonorities[index]:
                return index
        return None
