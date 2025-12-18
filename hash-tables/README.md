# Hash Tables

## What is a Hash Table?

A **hash table** (also called hash map or dictionary) is a data structure that stores key-value pairs. It uses a **hash function** to compute an index (hash code) where the value should be stored or retrieved.

Think of it like a library catalog system: you give the librarian a book title (key), and they know exactly which shelf (index) to find it on!

## Why Hash Tables Matter

Hash tables are incredibly powerful because they provide:
- **Fast lookups** - Find any value in O(1) average time
- **Flexible keys** - Use strings, numbers, or custom objects as keys
- **Dynamic sizing** - Grow automatically as needed
- **Associative storage** - Perfect for mapping relationships

## How Hash Tables Work

### The Hash Function

A hash function takes a key and converts it to an index:

```
hash("apple") → 5
hash("banana") → 2
hash("cherry") → 8

Table: [_, _, banana, _, _, apple, _, _, cherry, _]
Index:  0  1    2     3  4   5     6  7    8     9
```

### Collision Handling

When two keys hash to the same index, we have a **collision**. Two common solutions:

#### 1. Chaining
Store multiple items at the same index using a linked list:
```
Index 5 → [("apple", 1.50)] → [("avocado", 2.00)]
```

#### 2. Open Addressing
Find the next available slot:
```
If index 5 is taken, try 6, then 7, then 8, etc.
```

## Implementation

### Using Python Dictionary

Python dictionaries are hash tables:

```python
# Creating a hash table
prices = {
    "apple": 1.50,
    "banana": 0.75,
    "cherry": 3.00
}

# Adding/Updating
prices["date"] = 2.50
prices["apple"] = 1.75  # Update existing

# Accessing
print(prices["banana"])  # 0.75

# Checking existence
if "grape" in prices:
    print("Found!")

# Removing
del prices["cherry"]

# Iterating
for fruit, price in prices.items():
    print(f"{fruit}: ${price}")
```

### Custom Hash Table (Educational)

```python
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash(self, key):
        """Simple hash function"""
        return hash(key) % self.size
    
    def put(self, key, value):
        """Insert or update key-value pair"""
        index = self._hash(key)
        bucket = self.table[index]
        
        # Update if key exists
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        # Add new key-value pair
        bucket.append((key, value))
    
    def get(self, key):
        """Retrieve value by key"""
        index = self._hash(key)
        bucket = self.table[index]
        
        for k, v in bucket:
            if k == key:
                return v
        
        raise KeyError(f"Key '{key}' not found")
    
    def remove(self, key):
        """Delete key-value pair"""
        index = self._hash(key)
        bucket = self.table[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return
        
        raise KeyError(f"Key '{key}' not found")
```

## Common Operations

| Operation | Average Case | Worst Case |
|-----------|--------------|------------|
| Insert    | O(1)         | O(n)       |
| Search    | O(1)         | O(n)       |
| Delete    | O(1)         | O(n)       |

*Worst case occurs when all keys hash to the same index*

## Real-World Applications

### 1. Caching
```python
cache = {}

def expensive_computation(n):
    if n in cache:
        return cache[n]  # Fast retrieval!
    
    result = n * n  # Expensive operation
    cache[n] = result
    return result
```

### 2. Counting Frequencies
```python
text = "hello world"
freq = {}

for char in text:
    freq[char] = freq.get(char, 0) + 1

# freq = {'h': 1, 'e': 1, 'l': 3, 'o': 2, ...}
```

### 3. Grouping Data
```python
students = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Charlie", "Math"),
    ("Diana", "Science")
]

by_subject = {}
for name, subject in students:
    if subject not in by_subject:
        by_subject[subject] = []
    by_subject[subject].append(name)

# by_subject = {'Math': ['Alice', 'Charlie'], 
#               'Science': ['Bob', 'Diana']}
```

### 4. Phone Book
```python
contacts = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9012"
}

# O(1) lookup by name
print(contacts["Alice"])  # "555-1234"
```

## Load Factor

**Load factor** = Number of entries / Table size

- Low load factor (< 0.5): Fast but wastes space
- High load factor (> 0.75): Space-efficient but slower
- Python dicts automatically resize when load factor exceeds 2/3

## Hash Table vs Array

| Feature | Array | Hash Table |
|---------|-------|------------|
| Access by index | O(1) | N/A |
| Access by key | O(n) | O(1) |
| Ordered | Yes | No (usually) |
| Memory | Compact | Extra overhead |
| Use when | Position matters | Fast lookup by key |

## Common Patterns

### 1. Two Sum Pattern
Use hash table to store complements:
```python
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
```

### 2. Anagram Detection
Use sorted string or character count as key:
```python
def group_anagrams(words):
    groups = {}
    for word in words:
        key = ''.join(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())
```

## Practice Problems

Each problem is organized in its own directory containing:
- `problemN.md` - Problem description and examples
- `problemN.py` - Python starter file with function stubs and comments
- `test_problemN.py` - Pytest test file for validation

Navigate to each Problem directory to access the files:

- [Problem 1](./Problem%201/problem1.md)
- [Problem 2](./Problem%202/problem2.md)
- [Problem 3](./Problem%203/problem3.md)
- [Problem 4](./Problem%204/problem4.md)
- [Problem 5](./Problem%205/problem5.md)
- [Problem 6](./Problem%206/problem6.md)

## Next Steps

After hash tables, explore [Trees](../trees/) for hierarchical data organization!

---

💡 **Pro Tip**: Hash tables are your best friend for problems involving counting, grouping, or fast lookups. When you see "find pairs that sum to X" or "count frequency of elements," think hash table!
