import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from roman_numerals import from_roman, to_roman


def test_roundtrip():
    assert to_roman(1994) == "MCMXCIV"
    assert from_roman("MCMXCIV") == 1994
    for n in range(1, 200):
        assert from_roman(to_roman(n)) == n
