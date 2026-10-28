import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest

from bmi_calculator import bmi, category


def test_bmi():
    assert bmi(70, 1.75) == 22.9
    assert category(22.9) == "Normal"
    assert category(17) == "Underweight"
    assert category(31) == "Obese"


def test_bad_height():
    with pytest.raises(ValueError):
        bmi(70, 0)
