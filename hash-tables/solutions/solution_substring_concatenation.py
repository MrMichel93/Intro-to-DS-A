'''Solution: Substring with Concatenation (Challenge 5)'''
from collections import Counter

def find_substring(s, words):
    if not words:
        return []
    word_len = len(words[0])
    word_count = len(words)
    total_len = word_len * word_count
    word_freq = Counter(words)
    result = []
    
    for i in range(len(s) - total_len + 1):
        seen = Counter()
        for j in range(word_count):
            start = i + j * word_len
            word = s[start:start + word_len]
            if word not in word_freq:
                break
            seen[word] += 1
            if seen[word] > word_freq[word]:
                break
        if seen == word_freq:
            result.append(i)
    return result
