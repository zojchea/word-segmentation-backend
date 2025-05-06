from enum import Enum


class Phoneme(Enum):
    """
    Enumeration representing phonemes in Macedonian language and their phoneme
    sonority values.

    """
    A = "А", 12
    B = "Б", 2
    V = "В", 2
    G = "Г", 2
    D = "Д", 2
    GJ = "Ѓ", 2
    E = "Е", 12
    ZH = "Ж", 2
    Z = "З", 2
    DZ = "S", 2
    I = "И", 12
    J = "Ј", 3
    K = "К", 1
    L = "Л", 3
    LJ = "Љ", 3
    M = "М", 3
    N = "Н", 3
    NJ = "Њ", 3
    O = "О", 12
    P = "П", 1
    R = "Р", 5
    S = "С", 1
    T = "Т", 1
    KJ = "Ќ", 1
    U = "У", 12
    F = "Ф", 1
    H = "Х", 1
    C = "Ц", 1
    CH = "Ч", 1
    DJ = "Џ", 2
    SH = "Ш", 1
    APOSTROPHE = "`", 0
    FC = "FC", 0

    @classmethod
    def __getitem__(cls, item):
        """
        Retrieves an enum member based on the item.

        Args:
            item (str or int): The item to be retrieved.

        Returns:
            Enum member: The enum member corresponding to the item.

        Raises:
            KeyError: If the item is not found in the enumeration.
        """
        if isinstance(item, str):
            for member in cls:
                if member.value[0] == item:
                    return member
        return super().__getitem__(item)
