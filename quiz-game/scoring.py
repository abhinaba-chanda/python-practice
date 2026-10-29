"""Score helpers for the quiz."""


def percentage(correct, total):
    return 0 if total == 0 else round(100 * correct / total)


def grade(correct, total):
    p = percentage(correct, total)
    if p >= 90:
        return "Excellent"
    if p >= 70:
        return "Good"
    if p >= 50:
        return "Pass"
    return "Try again"
