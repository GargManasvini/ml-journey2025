from collections import Counter

def count_word_frequency(word_list):
    return Counter(word_list)

words = ['apple', 'banana', 'apple', 'apple', 'papaya']
print(count_word_frequency(words))