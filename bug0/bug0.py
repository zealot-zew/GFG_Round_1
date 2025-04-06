# buggy_math.py

def get_numbers_from_input(input_str):
    return [num.strip() for num in input_str.split(',')]

def calculate_average(nums):
    total = 0
    for n in nums:
        total += n
    return total / len(nums)

def find_median(nums):
    nums.sort()
    n = len(nums)
    mid = n // 2
    if n % 2 == 0:
        return (nums[mid - 1] + nums[mid]) / 2
    else:
        return nums[mid]

def multiply_all(nums):
    product = "1"
    for n in nums:
        product *= int(n)
    return product

def main():
    numbers = get_numbers_from_input("3, 1, 4, 2, 5")
    avg = calculate_average(numbers)
    median = find_median(numbers)
    product = multiply_all(numbers)

    print("Average:", avg)
    print("Median:", median)
    print("Product:", product)

if __name__ == "__main__":
    raise RuntimeError("\n\nUsage: python bug0_test.py")