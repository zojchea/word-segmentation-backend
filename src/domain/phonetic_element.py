from src.domain.phoneme import Phoneme


class PhoneticElement:

    def __init__(self, phoneme: Phoneme):
        """
        Initializes a PhoneticElement object from the given Phoneme.

        Args:
            phoneme (Phoneme): The Phoneme associated with the PhoneticElement.

        Returns:
            None.
        """
        self.phoneme = phoneme.value[0]
        self.phoneme_sonority = phoneme.value[1]
        self.triplet_difference = None

    def is_vowel(self):
        """
        Checks if the PhoneticElement represents a vowel.

        Returns:
            bool: True if the PhoneticElement represents a vowel, False otherwise.
        """
        return self.phoneme_sonority == 12

    def is_r(self):
        """
        Checks if the PhoneticElement represents the phoneme 'R'.

        Returns:
            bool: True if the PhoneticElement represents 'R', False otherwise.
        """
        return self.phoneme == Phoneme.R

    def is_special_character(self):
        """
        Checks if the PhoneticElement represents a special character.

        Returns:
            bool: True if the PhoneticElement represents a special character, False otherwise.
        """
        return self.phoneme_sonority == 0
