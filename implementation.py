# This would be in your e.g. implementation.py
def sum_of_three_numbers(num1, num2, num3):
    return num1 + num2 + num3


# This would be in your test_implementation.py
def test_sum_of_three_numbers():
    # 1. Setup the variables used in the test
    num1 = 2
    num2 = 3
    num3 = 5
    
    # 2. Call the functionality you want to test
    result = sum_of_three_numbers(num1, num2, num3)
    
    # 3. Verify that the outcome is expected
    assert result == 10