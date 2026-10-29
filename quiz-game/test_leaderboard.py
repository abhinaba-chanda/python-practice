from leaderboard import add_score, load


def test_leaderboard(tmp_path):
    p = str(tmp_path / "scores.json")
    assert load(p) == []
    add_score(p, "a", 3)
    board = add_score(p, "b", 5, keep=1)
    assert board == [{"name": "b", "score": 5}]
