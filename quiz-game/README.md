# Quiz Game

A small multiple choice quiz game for the terminal. Questions live in `questions.json`, so adding new ones needs no code change.

Moved here from my [python-quiz-game](https://github.com/abhinaba-chanda/python-quiz-game) repo so all my Python practice lives in one place.

## Play

```bash
cd quiz-game
python quiz.py
```

You get 5 random questions and a score at the end.

## Files

| File | What it does |
|---|---|
| `quiz.py` | Loads questions, asks them and checks answers |
| `questions.json` | The question bank |
| `scoring.py` | Score and percentage helpers |
| `shuffle.py` | Shuffles answer options |
| `leaderboard.py` | Keeps a top 5 leaderboard in a JSON file |

## Tests

```bash
pytest quiz-game
```
