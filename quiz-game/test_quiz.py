from quiz import check_answer, grade, load_questions, play

Q = {"question": "2+2?", "options": ["3", "4"], "answer": 1}


def test_check_answer():
    assert check_answer(Q, "b")
    assert check_answer(Q, " B ")
    assert not check_answer(Q, "a")
    assert not check_answer(Q, "")
    assert not check_answer(Q, "1")


def test_grade():
    assert grade(5, 5) == "Excellent"
    assert grade(3, 5) == "Good"
    assert grade(1, 5) == "Keep practicing"


def test_questions_file_is_valid():
    qs = load_questions()
    assert len(qs) >= 10
    for q in qs:
        assert 0 <= q["answer"] < len(q["options"])


def test_play_all_correct():
    answers = iter(["b"])
    assert play([Q], ask=lambda _: next(answers), rounds=1) == 1
