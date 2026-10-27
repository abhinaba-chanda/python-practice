"""Run with:  python -m pytest"""
import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from grade_calculator import average, grade  # noqa: E402
from leap_year import is_leap, leap_years_between  # noqa: E402
from temperature_converter import c_to_f, f_to_c  # noqa: E402
from vowel_counter import count_vowels, vowel_breakdown  # noqa: E402
from word_frequency import top_words, word_counts  # noqa: E402


def test_temperature():
    assert c_to_f(0) == 32
    assert c_to_f(100) == 212
    assert f_to_c(98.6) == 37
    assert f_to_c(c_to_f(25)) == 25


def test_vowels():
    assert count_vowels("Abhinaba") == 4
    assert count_vowels("rhythm") == 0
    assert vowel_breakdown("Messi") == {"a": 0, "e": 1, "i": 1, "o": 0, "u": 0}


@pytest.mark.parametrize("year,expected", [(2024, True), (2026, False), (2000, True), (1900, False)])
def test_leap(year, expected):
    assert is_leap(year) is expected


def test_leap_range():
    assert leap_years_between(2020, 2030) == [2020, 2024, 2028]


def test_grades():
    assert grade(95) == "A+"
    assert grade(80) == "A"
    assert grade(49.5) == "F"
    assert average([70, 80, 90]) == 80
    with pytest.raises(ValueError):
        grade(101)
    with pytest.raises(ValueError):
        average([])


def test_word_frequency():
    text = "Visca Barca! Visca, visca el Barca."
    assert word_counts(text)["visca"] == 3
    assert top_words(text, 2) == [("visca", 3), ("barca", 2)]
