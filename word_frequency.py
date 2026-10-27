# Word frequency counter
# Finds the most common words in a piece of text.
# Practice: string cleaning, dictionaries, sorting with a key.
import string


def word_counts(text):
    """Count every word, ignoring case and punctuation."""
    cleaned = text.lower().translate(str.maketrans("", "", string.punctuation))
    counts = {}
    for word in cleaned.split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def top_words(text, n=3):
    """The n most common words as (word, count), ties sorted alphabetically."""
    counts = word_counts(text)
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:n]


if __name__ == "__main__":
    text = input("Paste some text: ")
    for word, count in top_words(text, 5):
        print(f"{word}: {count}")
