from bug0.bug0 import (
    get_numbers_from_input,
    calculate_average,
    find_median,
    multiply_all
)
from link import show_pretty_link

def test_all_functions():
    try:
        # Test input
        input_str = "3, 1, 4, 2, 5"

        # Step 1: Get numbers
        numbers = get_numbers_from_input(input_str)
        if not all(isinstance(n, (int, float)) for n in numbers):
            raise TypeError("")

        # Step 2: Calculate average
        avg = calculate_average(numbers)
        if not isinstance(avg, (int, float)):
            raise TypeError("")

        # Step 3: Find median
        median = find_median(numbers)
        if not isinstance(median, (int, float)):
            raise TypeError("")

        # Step 4: Multiply all
        product = multiply_all(numbers)
        if not isinstance(product, (int, float)):
            raise TypeError("")

        show_pretty_link()

    except Exception:
        print("TRY AGAIN")

test_all_functions()
