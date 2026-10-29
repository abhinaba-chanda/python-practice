"""Shuffle answer options while tracking the correct one."""
import random


def shuffle_options(options, answer, seed=None):
    rng = random.Random(seed)
    shuffled = list(options)
    rng.shuffle(shuffled)
    return shuffled, shuffled.index(answer)
