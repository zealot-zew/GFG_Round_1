def get_numbers_from_input(input_str):
    # Convert to list of floats
    return [float(num.strip()) for num in input_str.split(',')]

def calculate_average(nums):
    total = 0
    for n in nums:
        total += n  # now n is float/int, so this works
    return total / len(nums)

def find_median(nums):
    # Sort the numbers properly (in-place)
    sorted_nums = sorted(nums)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        return sorted_nums[mid]

def multiply_all(nums):
    product = 1
    for n in nums:
        product *= n
    return product

def main():
    numbers = get_numbers_from_input("3, 1, 4, 2, 5")
    avg = calculate_average(numbers)
    median = find_median(numbers)
    product = multiply_all(numbers)

    print("Average:", avg)
    print("Median:", median)
    print("Product:", product)
