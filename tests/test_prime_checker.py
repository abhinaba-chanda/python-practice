import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from prime_checker import is_prime, primes_up_to


def test_is_prime():
    assert is_prime(2) and is_prime(13)
    assert not is_prime(1) and not is_prime(15)


def test_primes_up_to():
    assert primes_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]
