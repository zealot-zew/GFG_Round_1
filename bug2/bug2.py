def is_digit_palindrome(n):
    str_n = str(n)
    return is_palindrom(str_n)

def is_palindrom(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrom(s[1:-1])

def digit_sum(n):
    if n < 10:
        return n
    return n % 10 + digit_sum(n // 10)

def special_sum(n):
    total = digit_sum(n)
    if is_digit_palindrome(total):
        return calculate_modified_sum(n)
    else:
        return total * 2

def calculate_modified_sum(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return n + calculate_modified_sum(n - 2)
    else:
        return n + calculate_modified_sum(n - 1)

def main():
    num = int(input("Enter a number: "))
    result = special_sum(num)
    print("The special result is:", result)

if __name__ == "__main__":
    raise RuntimeError("\n\nUsage: python bug2_test.py\n\n")

