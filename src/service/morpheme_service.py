from src.repository.word_repository import WordRepository


class MorphemeService:
    """
    The MorphemeService class encapsulates the logic for segmenting a word
    into its constituent morphemes: prefix, root, suffix, and flexion.

    Attributes:
        __word_repository (WordRepository): An instance of WordRepository used to get
            prefixes, suffixes and flexions.

    Methods:
        divide_word_by_morphemes(word: str) -> str:
            Orchestrates the segmentation of a word into morphemes.

        find_and_cut_prefix(word: str) -> tuple:
            Identifies and extracts the prefix from a word.

        find_and_cut_flexion(word: str) -> tuple:
            Identifies and extracts the flexion from a word.

        find_and_cut_suffix(word_without_flexion: str) -> tuple:
            Identifies and extracts the suffix from a word without flexion.
    """

    def __init__(self, word_repository: WordRepository):
        """
        Initializes a MorphemeService object with a WordRepository instance.

        Args:
            word_repository (WordRepository): An instance of the WordRepository.

        Returns:
            None.
        """
        self.__word_repository = word_repository

    def divide_word_by_morphemes(self, word: str) -> str:
        """
        Divides a word into morphemes.

        Args:
            word (str): The word to be divided.

        Returns:
            str: The divided word represented as a string.

        """
        word = word.upper()
        prefix, word_without_prefix = self.find_and_cut_prefix(word=word)
        flexion, word_without_flexion = self.find_and_cut_flexion(word=word_without_prefix)
        suffix, root = self.find_and_cut_suffix(word_without_flexion=word_without_flexion)

        divided_word = ""
        if prefix:
            divided_word += f"{prefix}"

        if root:
            if divided_word != "":
                divided_word += "-"
            divided_word += root

        if suffix:
            if divided_word != "":
                divided_word += "-"
            divided_word += f"{suffix}"

        if flexion:
            if divided_word != "":
                divided_word += "-"
            divided_word += f"{flexion}"

        return divided_word

    def find_and_cut_prefix(self, word: str) -> tuple:
        """
        Finds and cuts the prefix from the given word.

        Args:
            word (str): The word to search for prefixes.

        Returns:
            tuple: A tuple containing the prefix (if found) and the word without the prefix.

        """
        for prefix in self.__word_repository.get_prefixes():
            if word.startswith(prefix):
                return prefix, word[len(prefix):]
        return None, word

    def find_and_cut_flexion(self, word) -> tuple:
        """
        Finds and cuts the flexion from the given word.

        Args:
            word: The word to search for flexions.

        Returns:
            tuple: A tuple containing the flexion (if found) and the word without the flexion.

        """
        for flexion in self.__word_repository.get_flexions():
            if word.endswith(flexion):
                return flexion, word[:-len(flexion)]
        return None, word

    def find_and_cut_suffix(self, word_without_flexion) -> tuple:
        """
        Finds and cuts the suffix from the given word without flexion.

        Args:
            word_without_flexion: The word without flexion to search for suffixes.

        Returns:
            tuple: A tuple containing the suffix (if found) and the word without the suffix.

        """
        for suffix in self.__word_repository.get_suffixes():
            if word_without_flexion.endswith(suffix):
                return suffix, word_without_flexion[:-len(suffix)]
        return None, word_without_flexion
