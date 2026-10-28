import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from number_to_words import to_words


def test_words():
    assert to_words(7) == "seven"
    assert to_words(42) == "forty-two"
    assert to_words(300) == "three hundred"
    assert to_words(515) == "five hundred and fifteen"
