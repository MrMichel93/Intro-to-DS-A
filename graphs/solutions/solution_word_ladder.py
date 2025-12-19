'''Solution: Word Ladder (Challenge 5)'''
from collections import deque, defaultdict

def ladder_length(begin_word, end_word, word_list):
    if end_word not in word_list:
        return 0
    
    word_list = set(word_list)
    queue = deque([(begin_word, 1)])
    
    while queue:
        word, length = queue.popleft()
        if word == end_word:
            return length
        
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i+1:]
                if next_word in word_list:
                    word_list.remove(next_word)
                    queue.append((next_word, length + 1))
    return 0
