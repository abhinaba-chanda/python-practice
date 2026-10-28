import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from palindrome import is_palindrome


def test_palindrome():
    assert is_palindrome("racecar")
    assert is_palindrome("A man, a plan, a canal: Panama")
    assert not is_palindrome("python")
