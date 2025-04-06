from bug2 import (
    is_digit_palindrome,
    digit_sum,
    special_sum,
    calculate_modified_sum
)
from link import show_pretty_link

def test_special_sum_module():
    try:
        # Test digit_sum
        if digit_sum(123) != 6:
            raise ValueError("")

        if digit_sum(0) != 0:
            raise ValueError("")

        # Test is_digit_palindrome
        if not is_digit_palindrome(121):
            raise ValueError("")

        if is_digit_palindrome(123):
            raise ValueError("")

        # Test calculate_modified_sum
        if calculate_modified_sum(4) != 6:  # 4 + 2 + 0
            raise ValueError("")

        if calculate_modified_sum(3) != 6:  # 3 + 2 + 1 + 0
            raise ValueError("")

        # Test special_sum
        if special_sum(121) != calculate_modified_sum(121):
            raise ValueError("")

        if special_sum(123) != digit_sum(123) * 2:
            raise ValueError("")

        show_pretty_link()

    except Exception as e:
        print("TRY AGAIN")

test_special_sum_module()
