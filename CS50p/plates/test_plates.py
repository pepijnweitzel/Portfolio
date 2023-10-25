# Code created by Pepijn Weitzel
from plates import is_valid

def test_two_letters():
    assert is_valid("BA1232") == True
    assert is_valid("B12323") == False

def test_max_six():
    assert is_valid("BADS12") == True
    assert is_valid("BAJDLSES") == False

def test_numbers_middle():
    assert is_valid("BA12DA") == False

def test_no_periods():
    assert is_valid("BA!?DA") == False

def test_no_input():
    assert is_valid("") == False