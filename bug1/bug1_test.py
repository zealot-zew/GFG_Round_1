from bug1 import (
    sum_list_recursive,
    factorial,
    flatten_list,
    reverse_string
)

from link import show_pretty_link

def test_all_recursive_functions():
    try:
        # Test sum_list_recursive
        result_sum = sum_list_recursive([1, 2, 3])
        if not isinstance(result_sum, (int, float)):
            raise TypeError("sum_list_recursive should return a number")
        if result_sum != 6:
            raise ValueError(f"Expected sum 6, got {result_sum}")

        # Test factorial
        result_fact = factorial(0)
        if not isinstance(result_fact, int):
            raise TypeError("factorial should return an integer")
        if result_fact != 1:
            raise ValueError(f"Expected factorial(0) to be 1, got {result_fact}")

        # Test flatten_list
        result_flat = flatten_list([1, [2, [3]], 4])
        if result_flat != [1, 2, 3, 4]:
            raise ValueError(f"Expected flattened list [1, 2, 3, 4], got {result_flat}")

        # Test reverse_string
        result_rev = reverse_string("hello")
        if not isinstance(result_rev, str):
            raise TypeError("reverse_string should return a string")
        if result_rev != "olleh":
            raise ValueError(f"Expected 'olleh', got {result_rev}")

        show_pretty_link()

    except Exception as e:
        print("TRY AGAIN")

test_all_recursive_functions()
