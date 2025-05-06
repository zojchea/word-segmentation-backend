class WordRepository:

    def __init__(self):
        """
        Initializes a WordRepository object with lists of prefixes, flexions, and suffixes.

        Args:
            None.

        Returns:
            None.
        """
        self.prefixes = ["ПОД", "ПО", "ПРЕД", "НА", "НАЈ", "ОД", "НЕ", "ИЗ"]
        self.flexions = ["ТА", "Е", "АТ"]
        self.suffixes = ["СКИ", "СКА", "СТВЕН", "СТВО", "КА", "УВА", "СТВА"]

    def get_prefixes(self) -> list[str]:
        """
        Retrieves the list of prefixes.

        Args:
            None.

        Returns:
            list[str]: The list of prefixes.

        """
        return self.prefixes

    def get_flexions(self) -> list[str]:
        """
        Retrieves the list of flexions.

        Args:
            None.

        Returns:
            list[str]: The list of flexions.

        """
        return self.flexions

    def get_suffixes(self) -> list[str]:
        """
        Retrieves the list of suffixes.

        Args:
            None.

        Returns:
            list[str]: The list of suffixes.

        """
        return self.suffixes
