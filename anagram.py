"""Check if two words are anagrams and group anagrams."""
from collections import defaultdict


def key(word):
    return "".join(sorted(word.lower().replace(" ", "")))


def is_anagram(a, b):
    return key(a) == key(b)


def group_anagrams(words):
    groups = defaultdict(list)
    for w in words:
        groups[key(w)].append(w)
    return list(groups.values())
