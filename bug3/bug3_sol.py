# mystery_bugs.py (Fixed)

def word_count(sentence):
    words = sentence.split(" ")
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1  # ✅ initialize with 1
    return counts

def collect_items(item, basket=None):
    if basket is None:
        basket = []  # ✅ avoid shared mutable default
    basket.append(item)
    return basket

def is_even_sum(lst):
    return sum(lst) % 2 == 0  # ✅ remove extra `and sum(lst)`

def remove_vowels(word):
    vowels = "aeiou"
    for v in vowels:
        word = word.replace(v, "")  # ✅ reassign the result
    return word

def bad_recursion(n):
    if n <= 0:
        return 0
    return n + bad_recursion(n - 1)  # ✅ fix typo in recursive call
