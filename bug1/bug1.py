# buggy_recursive.py

def sum_list_recursive(lst):
    if lst == None:
        return 0
    if len(lst) == 0:
        return []
    return lst[0] + sum_list_recursive(lst[1:])

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

def flatten_list(nested):
    flat = []
    for item in nested:
        if isinstance(item, list):
            flat += flatten_list(item)
        else:
            flat.append(item)
    return flat

def reverse_string(s):
    if len(s) == 0:
        return []
    return reverse_string(s[1:]) + [s[0]]

def main():
    print("Sum:", sum_list_recursive([1, 2, 3, 4]))
    print("Factorial of 0:", factorial(0))
    print("Flatten:", flatten_list([1, [2, [3, 4]], 5]))
    print("Reversed:", reverse_string("hello"))


if __name__ == "__main__":
    raise RuntimeError("\n\nUsage: python bug1_test.py")