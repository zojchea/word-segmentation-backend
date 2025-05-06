import json
import pandas as pd

from src.mapper.string_to_word_mapper import StringToWordMapper
from src.service.syllable_service import SyllableService


def analyze_syllable_divisions():
    """Analytics for divide_word_by_syllables method of SyllableService."""

    try:
        with open("test-words.json", 'r') as file:
            words = json.load(file)
    except FileNotFoundError:
        print("The file was not found. Please provide a valid file path.")
        return
    except json.JSONDecodeError:
        print("There was an error decoding the JSON file. Please ensure the file is properly formatted.")
        return

    correct = 0
    false = 0
    incorrect_divisions = []

    string_to_word_mapper = StringToWordMapper()
    syllable_service = SyllableService()

    for word_obj in words:
        word_str = word_obj["word"]

        word = string_to_word_mapper.map_to_word(word_str=word_str)
        divided_by_syllables = syllable_service.divide_word_by_syllables(
            word=word
        )
        expected = word_obj["wordBySyllables"].upper()

        if divided_by_syllables == expected:
            correct = correct + 1
        else:
            false = false + 1
            incorrect_divisions.append([word_str.upper(), divided_by_syllables, expected])
            print(f"Expected: {expected}")
            print(f"Actual: {divided_by_syllables}")
            print()

    df = pd.DataFrame(incorrect_divisions, columns=['Word', 'Actual', 'Expected'])
    df.to_excel('incorrect_syllable_divisions.xlsx', index=False)
    
    print(f"Correct: {correct}; {round((correct/(correct + false))*100, 2)}%")
    print(f"False: {false}; {round((false/(correct + false))*100, 2)}%")


if __name__ == "__main__":
    analyze_syllable_divisions()
