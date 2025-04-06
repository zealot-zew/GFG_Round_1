from bug3 import (
    word_count,
    collect_items,
    is_even_sum,
    remove_vowels,
    bad_recursion
)
from link import show_pretty_link

def test_buggy_code():
    try:
        # Test word_count
        wc = word_count("hello world hello")
        if wc.get("hello") != 2 or wc.get("world") != 1:
            raise ValueError("")

        # Test collect_items
        b1 = collect_items("apple")
        b2 = collect_items("banana")
        if b1 is b2 and len(b2) != 1:
            raise ValueError("")

        # Test is_even_sum
        even = is_even_sum([2, 4])
        if even is not True:
            raise ValueError("")

        # Test remove_vowels
        no_vowels = remove_vowels("beautiful")
        if no_vowels != "btfl":
            raise ValueError("")

        # Test bad_recursion
        total = bad_recursion(5)
        if total != 15:
            raise ValueError("")

        show_pretty_link()

    except Exception as e:
        print("TRY AGAIN")

test_buggy_code()
