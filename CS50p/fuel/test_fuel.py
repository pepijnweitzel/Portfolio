# Code created by Pepijn Weitzel
from fuel import gauge, convert
import pytest

def test_convert():
    assert convert("12/24") == 50
    with pytest.raises(ValueError):
        convert("24/12")
        convert("pe/at")
    with pytest.raises(ZeroDivisionError):
        convert("12/0")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(23) == "23%"