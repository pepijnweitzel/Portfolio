# Code created by Pepijn Weitzel

from jar import Jar
import pytest

def test_init():
    with pytest.raises(ValueError):
        Jar("cat")
    jar = Jar()
    assert jar.capacity() == "12"

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪"
