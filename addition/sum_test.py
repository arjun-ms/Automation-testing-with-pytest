import pytest

def sum():
    num1 = 10
    num2 = 15    
    return num1+num2

def test_sum():
    assert sum() == 30