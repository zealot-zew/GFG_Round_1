def is_digit_palindrome(n):
    str_n = str(n)
    return is_palindrome(str_n)  # ✅ Fixed name

def is_palindrome(s):  # ✅ Fixed typo
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

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
    if n == 0:  # ✅ Fixed '=' to '=='
        return 0
    if n % 2 == 0:
        return n + calculate_modified_sum(n - 2)
    else:
        return n + calculate_modified_sum(n - 1)
