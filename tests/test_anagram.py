import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from anagram import group_anagrams, is_anagram


def test_is_anagram():
    assert is_anagram("listen", "silent")
    assert is_anagram("Dormitory", "dirty room")
    assert not is_anagram("apple", "paper")


def test_group():
    assert group_anagrams(["eat", "tea", "tan", "nat"]) == [["eat", "tea"], ["tan", "nat"]]
