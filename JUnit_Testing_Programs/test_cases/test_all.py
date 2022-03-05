# from JUnit_Testing_Programs.DayOfWeek import day_of_week
from JUnit_Testing_Programs.swap_nibbles import decimal_to_binary,binary_to_decimal

# It's tuesday on 22/2/22, therefore is should return 2
# def test_dayOfWeek():
#     assert day_of_week(22,2,2022) == 2

#100 --> '1100100'
def test_decimal_to_binary():
    assert decimal_to_binary(100) == '1100100'

# '1001100' --> 76
def test_binary_to_decimal():
    assert binary_to_decimal('1001100') == 76

print(decimal_to_binary(100))