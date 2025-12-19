# Module 5: Hash Tables - Checkpoint Quiz

**Time Limit:** 45 minutes  
**Total Points:** 100

## Instructions
- Answer all questions to the best of your ability
- For multiple choice questions, select the single best answer
- For code analysis questions, write your answer clearly
- For short answer questions, provide concise but complete responses

---

## Part 1: Multiple Choice Questions (40 points, 4 points each)

### Question 1
What is the average time complexity for insertion, deletion, and lookup in a hash table?
- A) O(1)
- B) O(log n)
- C) O(n)
- D) O(n²)

### Question 2
What is a hash function?
- A) A function that secures data
- B) A function that maps keys to array indices
- C) A function that sorts data
- D) A function that compresses data

### Question 3
What is a collision in a hash table?
- A) When the table runs out of space
- B) When two different keys hash to the same index
- C) When a key is deleted
- D) When the hash function fails

### Question 4
Which method handles collisions by storing multiple values at the same index in a linked list?
- A) Open addressing
- B) Linear probing
- C) Chaining
- D) Quadratic probing

### Question 5
What is the load factor of a hash table?
- A) The speed of the hash function
- B) The ratio of stored elements to table capacity
- C) The number of collisions
- D) The size of the table

### Question 6
What is linear probing?
- A) A collision resolution technique that searches for the next available slot linearly
- B) A hashing algorithm
- C) A way to delete elements
- D) A method to sort the table

### Question 7
What is a good characteristic of a hash function?
- A) Always returns 0
- B) Distributes keys uniformly across the table
- C) Is slow to compute
- D) Maps all keys to the same index

### Question 8
In Python, which built-in data structure implements a hash table?
- A) list
- B) tuple
- C) dict
- D) array

### Question 9
What happens when a hash table's load factor becomes too high?
- A) Performance improves
- B) More collisions occur, degrading performance
- C) The table automatically shrinks
- D) Nothing changes

### Question 10
Why can't all objects be used as dictionary keys in Python?
- A) They take too much memory
- B) They must be hashable (immutable)
- C) They are too slow
- D) Python doesn't allow it

---

## Part 2: Code Analysis Questions (30 points, 10 points each)

### Question 11
What will this code output? Explain what's happening.

```python
def count_frequency(words):
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
result = count_frequency(words)
print(result)
```

**Your Answer:**
- Output: _______________________________________________
- What does this function do? _______________
- Time Complexity: _______________
- Space Complexity: _______________

### Question 12
Analyze this simple hash table implementation. What collision resolution technique does it use?

```python
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self.hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))
```

**Your Answer:**
- Collision resolution technique: _______________
- Time complexity of insert (average case): _______________
- Time complexity of insert (worst case): _______________
- Explanation: _______________________________________________

### Question 13
Find the bug in this code that checks if two strings are anagrams:

```python
def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False
    
    char_count = {}
    
    for char in s1:
        char_count[char] = char_count.get(char, 0) + 1
    
    for char in s2:
        if char not in char_count:
            return False
        char_count[char] -= 1
    
    return True
```

**Your Answer:**
- Test case that fails: _______________
- Why it fails: _______________________________________________
- How to fix it: _______________________________________________

---

## Part 3: Short Answer Questions (30 points, 15 points each)

### Question 14
Explain how hash tables achieve O(1) average-case lookup time. What factors can degrade this performance to O(n)? Discuss the role of the hash function, load factor, and collision resolution strategy. (5-7 sentences)

**Your Answer:**
_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________

### Question 15
You're building a caching system for a web application that needs to store recently accessed pages. You need fast lookup by URL and want to limit the cache size to the 1000 most recently used pages. What data structures would you combine, and why? Explain how you would implement the eviction policy. (5-7 sentences)

**Your Answer:**
_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________

---

**End of Quiz**

Submit your completed quiz to your instructor. Good luck!
