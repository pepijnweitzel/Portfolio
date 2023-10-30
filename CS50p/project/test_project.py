# Code created by Pepijn Weitzel
from project import check_border_collision, check_collision, calculate_speed



def test_check_border_collision():
    assert check_border_collision(5, 50) == [5, 50]
    assert check_border_collision(-200, 50) == [0, 50]
    assert check_border_collision(700, 0) == [450,0]
    assert check_border_collision(5, 20) == [5, 50]
    assert check_border_collision(5, 800) == [5, 750]

def test_check_collision():
    assert check_collision(50, 50, 50, 50) == True
    assert check_collision(50, 350, 50, 50) == False

def test_calculate_speed():
    assert calculate_speed(4) == 2
    assert calculate_speed(50) == 4
    assert calculate_speed(9) == 3
