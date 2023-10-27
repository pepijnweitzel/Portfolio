# Code created by Pepijn Weitzel

from um import count


def test_nothing():
    assert count("") == 0
    assert count("Hey umpy how are you?") == 0

def test_start_um():
    assert count("Um, how do you do?") == 1
    assert count("um") == 1

def test_middle_um():
    assert count("Hey there, UM how do you do?") == 1
    assert count("Hey Um, do you know um him?") == 2
