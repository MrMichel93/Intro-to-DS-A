# Arrays

## What is an Array?

An **array** is a fundamental data structure that stores elements in contiguous memory locations. Think of it like a row of numbered boxes, where each box can hold a value, and you can access any box directly using its position (index).

## Why Arrays Matter

Arrays are everywhere in programming! They're used to:
- Store lists of items (like shopping lists, student names, or scores)
- Represent matrices and grids (like game boards)
- Build more complex data structures
- Process collections of data efficiently

## Key Characteristics

### 1. **Fixed Size** (in many languages)
Once created, the size cannot change. If you need more space, you create a new array.

### 2. **Indexed Access**
Elements are accessed using their position, starting from 0:
```
Array: [10, 20, 30, 40, 50]
Index:  0   1   2   3   4
```

### 3. **Same Data Type**
All elements in an array typically have the same data type (integers, strings, etc.)

### 4. **Contiguous Memory**
Elements are stored next to each other in memory, making access very fast.

## Common Operations

### Accessing Elements
**Time Complexity: O(1)** - Constant time, super fast!

```python
# Python example
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Output: "apple"
print(fruits[2])  # Output: "cherry"
```

### Updating Elements
**Time Complexity: O(1)**

```python
fruits[1] = "blueberry"
# fruits is now ["apple", "blueberry", "cherry"]
```

### Searching for an Element
**Time Complexity: O(n)** - Must check each element in worst case

```python
def find_element(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1  # Not found
```

### Inserting/Deleting Elements
**Time Complexity: O(n)** - May need to shift many elements

## Real-World Applications

1. **Image Processing** - Images are 2D arrays of pixels
2. **Databases** - Tables can be represented as arrays
3. **Gaming** - Game boards, inventory systems
4. **Statistics** - Storing and analyzing data sets
5. **Buffers** - Temporary data storage in many applications

## Time Complexity Summary

| Operation | Time Complexity |
|-----------|----------------|
| Access    | O(1)           |
| Search    | O(n)           |
| Insert    | O(n)           |
| Delete    | O(n)           |

## Common Pitfalls

⚠️ **Index Out of Bounds** - Trying to access an index that doesn't exist
```python
arr = [1, 2, 3]
print(arr[5])  # Error! Only indices 0-2 exist
```

⚠️ **Off-by-One Errors** - Forgetting arrays start at index 0

## Practice Problems

Now it's your turn! Try these problems to test your understanding:

1. **[Problem 1: Find Maximum](./problem1.md)** - Easy 🟢
2. **[Problem 2: Reverse Array](./problem2.md)** - Easy 🟢
3. **[Problem 3: Two Sum](./problem3.md)** - Medium 🟡
4. **[Problem 4: Rotate Array](./problem4.md)** - Medium 🟡
5. **[Problem 5: Find Duplicates](./problem5.md)** - Medium 🟡
6. **[Problem 6: Merge Sorted Arrays](./problem6.md)** - Hard 🔴

## Next Steps

Once you're comfortable with arrays, move on to [Linked Lists](../linked-lists/), which offer more flexibility in size management!

---

💡 **Pro Tip**: Arrays are great when you know the size ahead of time and need fast access by index. If you need to frequently insert/delete elements, consider other data structures like Linked Lists!
