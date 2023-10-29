# Code created by Pepijn Weitzel

from jar import Jar
import pytest

def test_init():
    with pytest.raises(ValueError):
        Jar("cat")

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪"
    jar.withdraw(2)
    assert str(jar) == "🍪🍪🍪"

def test_deposit():
    jar = Jar()
    

def test_withdraw():
    ...
