"""Check whether a word or sentence is a palindrome."""


def clean(text):
    return "".join(ch.lower() for ch in text if ch.isalnum())


def is_palindrome(text):
    s = clean(text)
    return s == s[::-1]


if __name__ == "__main__":
    word = input("Enter text: ")
    print("Palindrome!" if is_palindrome(word) else "Not a palindrome.")
