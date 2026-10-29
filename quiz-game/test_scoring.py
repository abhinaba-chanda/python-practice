from scoring import grade, percentage


def test_scoring():
    assert percentage(3, 4) == 75
    assert percentage(0, 0) == 0
    assert grade(9, 10) == "Excellent"
    assert grade(1, 4) == "Try again"
