# Code created by Pepijn Weitzel

from working import convert
import pytest


def test_wrong_value():
    with pytest.raises(ValueError):
        convert("9AM - 5PM")
        convert(" to ")
        convert("13 PM to 18 AM")

def test_correct():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12 AM to 5 PM") == "00:00 to 17:00"
    assert convert("4 AM to 12 PM") == "04:00 to 12:00"

def test_correct_colon():
    assert convert("9:30 AM to 5:30 PM") == "09:30 to 17:30"
    assert convert("7:30 AM to 2:30 PM") == "07:30 to 14:30"
