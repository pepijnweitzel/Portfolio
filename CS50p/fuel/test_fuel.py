# Code created by Pepijn Weitzel
from fuel import gauge, convert
import pytest

def test_convert():
    assert convert("12/24") == 50
    with pytest.raises(ValueError):
        convert("24/12")
        convert("12/0")
        convert("pe/at")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(100) == "F"
    assert gauge(23) == "23%"