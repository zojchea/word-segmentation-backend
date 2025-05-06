from src.domain.phonetic_element import PhoneticElement


class Word:
    def __init__(self, phonetic_elements: list[PhoneticElement]):
        """
        Initializes a Word object with the given list of PhoneticElement and calculates
        and sets the triplet differences.

        Args:
            phonetic_elements (list[PhoneticElement]): The list of PhoneticElement.

        Returns:
            None.
        """
        self.phonetic_elements = phonetic_elements
        self.__set_triplet_differences()

    def __set_triplet_differences(self):
        """
        Calculates and sets the triplet differences for each PhoneticElement in the Word.

        Returns:
            None.
        """
        for index in range(0, len(self.phonetic_elements) - 1):
            previous_phonetic_element = self.get_previous_phonetic_element(current_index=index)
            current_phonetic_element = self.phonetic_elements[index]
            next_phonetic_element = self.get_next_phonetic_element(current_index=index)

            triplet_difference = current_phonetic_element.phoneme_sonority
            if previous_phonetic_element and next_phonetic_element:
                triplet_difference = triplet_difference - previous_phonetic_element.phoneme_sonority - next_phonetic_element.phoneme_sonority
            else:
                triplet_difference = None

            current_phonetic_element.triplet_difference = triplet_difference

    def get_previous_phonetic_element(self, current_index: int) -> PhoneticElement | None:
        """
        Retrieves the previous PhoneticElement in the Word based on the current index.

        Args:
            current_index (int): The current index.

        Returns:
            PhoneticElement or None: The previous PhoneticElement if it exists, None otherwise.
        """
        if current_index > 0:
            return self.phonetic_elements[current_index - 1]
        return None

    def get_next_phonetic_element(self, current_index: int) -> PhoneticElement | None:
        """
        Retrieves the next PhoneticElement in the Word based on the current index.

        Args:
            current_index (int): The current index.

        Returns:
            PhoneticElement or None: The next PhoneticElement if it exists, None otherwise.
        """
        if current_index < len(self.phonetic_elements) - 1:
            return self.phonetic_elements[current_index + 1]
        return None
