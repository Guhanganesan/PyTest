import math, pytest
 
# Test case 1
def test_cal_square_1():
    result = math.sqrt(25)
    assert result == 5
 
# Test case 2
def test_cal_square_2():
    result = math.sqrt(36)
    assert result == 6
 
 
# Test case 3
def test_cal_square_3():
    result = math.sqrt(49)
    assert result == 7
 
 
# Test case 4
def test_cal_square_4():
    result = math.sqrt(64)
    assert result == 8

# To avoid this in simple way
@pytest.mark.parametrize("test_input, expected_output", [(25, 5), (36, 6), (49, 7)])
def test_cal_square(test_input, expected_output):
    result = math.sqrt(test_input)
    assert result == expected_output