# Code created by Pepijn Weitzel

from seasons import get_difference, get_text
import datetime




def test_get_difference():
    assert get_difference(datetime.date.today()) == 0
    assert get_difference(datetime.date(2023, 10, 27)) == 1440


def test_get_text():
    assert get_text(0) == "Zero minutes"
    assert get_text(10) == "Ten minutes"
