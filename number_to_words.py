"""Convert numbers 0-999 into English words."""

ONES = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
        "seventeen", "eighteen", "nineteen"]
TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


def to_words(n):
    if not 0 <= n <= 999:
        raise ValueError("only 0-999 supported")
    if n < 20:
        return ONES[n]
    if n < 100:
        t, o = divmod(n, 10)
        return TENS[t] + ("" if o == 0 else "-" + ONES[o])
    h, rest = divmod(n, 100)
    return ONES[h] + " hundred" + ("" if rest == 0 else " and " + to_words(rest))
