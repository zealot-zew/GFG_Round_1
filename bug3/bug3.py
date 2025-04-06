# mystery_bugs.py

def word_count(sentence):
    words = sentence.split(" ")
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 0
    return counts

def collect_items(item, basket=[]):
    basket.append(item)
    return basket

def is_even_sum(lst):
    return sum(lst) % 2 == 0 and sum(lst)

def remove_vowels(word):
    vowels = "aeiou"
    for v in vowels:
        word.replace(v, "")
    return word

def bad_recursion(n):
    if n <= 0:
        return 0
    return n + bad_recusrion(n - 1)

if __name__ == "__main__":
    raise RuntimeError("\n\nUsage: python bug3_test.py\n\n")
