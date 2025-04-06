# buggy_recursive.py (Fixed)

def sum_list_recursive(lst):
    # Base case: empty list returns 0 (int)
    if lst is None or len(lst) == 0:
        return 0
    return lst[0] + sum_list_recursive(lst[1:])

def factorial(n):
    # Base case for 0 and 1
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def flatten_list(nested):
    flat = []
    for item in nested:
        if isinstance(item, list):
            flat.extend(flatten_list(item))  # Correctly flatten
        else:
            flat.append(item)
    return flat

def reverse_string(s):
    # Base case: empty string returns empty string
    if len(s) == 0:
        return ""
    return reverse_string(s[1:]) + s[0]

def main():
    print("Sum:", sum_list_recursive([1, 2, 3, 4]))
    print("Factorial of 5:", factorial(5))
    print("Flatten:", flatten_list([1, [2, [3, 4]], 5]))
    print("Reversed:", reverse_string("hello"))