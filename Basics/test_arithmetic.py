def test_greater():
    number = 3
    assert number > 5 

def test_lesser():
    number = 3
    assert number < 5

def test_greater_than_equal():
    number = 3
    assert 3 >= 3

def test_equal():
    number = 3
    assert number == 3

"""
def test_greater():
        number = 3
>       assert number > 5
E       assert 3 > 5

test_arithmetic.py:3: AssertionError
"""