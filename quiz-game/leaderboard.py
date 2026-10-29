"""Keep a top-N leaderboard in a JSON file."""
import json
import os


def load(path):
    if not os.path.exists(path):
        return []
    with open(path) as f:
        return json.load(f)


def add_score(path, name, score, keep=5):
    board = load(path)
    board.append({"name": name, "score": score})
    board.sort(key=lambda e: e["score"], reverse=True)
    board = board[:keep]
    with open(path, "w") as f:
        json.dump(board, f, indent=2)
    return board
