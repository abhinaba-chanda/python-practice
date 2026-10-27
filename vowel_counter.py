# Vowel counter
# Counts the vowels in a sentence and shows how many of each.
# Practice: strings, loops, dictionaries.

VOWELS = "aeiou"


def count_vowels(text):
    """Return the total number of vowels in text (upper or lower case)."""
    return sum(1 for ch in text.lower() if ch in VOWELS)


def vowel_breakdown(text):
    """Return a dict like {"a": 2, "e": 1, ...} for every vowel."""
    counts = {v: 0 for v in VOWELS}
    for ch in text.lower():
        if ch in counts:
            counts[ch] += 1
    return counts


if __name__ == "__main__":
    sentence = input("Type a sentence: ")
    print("Total vowels:", count_vowels(sentence))
    for vowel, n in vowel_breakdown(sentence).items():
        print(f"  {vowel}: {n}")
