from shuffle import shuffle_options


def test_shuffle_keeps_answer():
    opts, idx = shuffle_options(["a", "b", "c", "d"], "c", seed=3)
    assert sorted(opts) == ["a", "b", "c", "d"]
    assert opts[idx] == "c"
