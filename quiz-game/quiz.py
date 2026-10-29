"""Terminal quiz game: multiple choice questions loaded from questions.json."""
import json
import random
from pathlib import Path

QUESTIONS_FILE = Path(__file__).with_name("questions.json")


def load_questions(path=QUESTIONS_FILE):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def check_answer(question, choice):
    """Return True if choice (a letter like 'b') is the right option."""
    choice = choice.strip().lower()
    if len(choice) != 1 or not "a" <= choice <= "z":
        return False
    index = ord(choice) - ord("a")
    return index == question["answer"]


def grade(score, total):
    if total == 0:
        return "No questions"
    pct = score * 100 / total
    if pct >= 90:
        return "Excellent"
    if pct >= 60:
        return "Good"
    return "Keep practicing"


def play(questions, ask=input, rounds=5):
    picked = random.sample(questions, min(rounds, len(questions)))
    score = 0
    for n, q in enumerate(picked, 1):
        print(f"\nQ{n}. {q['question']}")
        for i, opt in enumerate(q["options"]):
            print(f"  {chr(ord('a') + i)}) {opt}")
        if check_answer(q, ask("Your answer: ")):
            print("Correct!")
            score += 1
        else:
            print("Wrong, answer: " + q["options"][q["answer"]])
    print(f"\nScore: {score}/{len(picked)} - {grade(score, len(picked))}")
    return score


if __name__ == "__main__":
    play(load_questions())
