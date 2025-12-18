# Sorting Algorithms

## What is Sorting?

**Sorting** is the process of arranging elements in a specific order (ascending or descending). It's one of the most fundamental operations in computer science.

```
Unsorted: [5, 2, 8, 1, 9]
Sorted:   [1, 2, 5, 8, 9]
```

## Why Sorting Matters

Sorting is crucial for:
- **Searching** - Binary search requires sorted data
- **Databases** - Query optimization
- **Data analysis** - Finding patterns
- **User interfaces** - Displaying organized information
- **Algorithms** - Many algorithms require sorted input

## Algorithm Comparison

| Algorithm | Best Case | Average Case | Worst Case | Space | Stable |
|-----------|-----------|--------------|------------|-------|--------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No |

**Stable**: Maintains relative order of equal elements

## Simple Sorting Algorithms

### 1. Bubble Sort
Repeatedly swap adjacent elements if they're in wrong order.

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  # Already sorted
    return arr

# Time: O(n²), Space: O(1)
# Good for: Small datasets, nearly sorted data
```

### 2. Selection Sort
Find minimum element and move to beginning.

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Time: O(n²), Space: O(1)
# Good for: Small datasets, minimal swaps needed
```

### 3. Insertion Sort
Build sorted array one element at a time.

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Time: O(n²) worst, O(n) best, Space: O(1)
# Good for: Small datasets, nearly sorted data, online sorting
```

## Efficient Sorting Algorithms

### 4. Merge Sort
Divide array in half, sort each half, merge them.

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Time: O(n log n) always, Space: O(n)
# Good for: Large datasets, stable sort needed, linked lists
```

### 5. Quick Sort
Pick pivot, partition around it, recursively sort.

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# More efficient in-place version:
def quick_sort_inplace(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_inplace(arr, low, pi - 1)
        quick_sort_inplace(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Time: O(n log n) average, O(n²) worst, Space: O(log n)
# Good for: Large datasets, in-place sorting, average case performance
```

### 6. Heap Sort
Build max heap, repeatedly extract maximum.

```python
def heap_sort(arr):
    n = len(arr)
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap
        heapify(arr, i, 0)
    
    return arr

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

# Time: O(n log n), Space: O(1)
# Good for: Guaranteed O(n log n), in-place sorting
```

## Specialized Sorting

### 7. Counting Sort
Count occurrences of each value (for integers in range).

```python
def counting_sort(arr):
    if not arr:
        return arr
    
    max_val = max(arr)
    count = [0] * (max_val + 1)
    
    # Count occurrences
    for num in arr:
        count[num] += 1
    
    # Build sorted array
    result = []
    for num in range(len(count)):
        result.extend([num] * count[num])
    
    return result

# Time: O(n + k) where k is range, Space: O(k)
# Good for: Small range of integers
```

### 8. Radix Sort
Sort by individual digits/characters.

```python
def radix_sort(arr):
    if not arr:
        return arr
    
    max_val = max(arr)
    exp = 1
    
    while max_val // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10
    
    return arr

def counting_sort_by_digit(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    for num in arr:
        digit = (num // exp) % 10
        count[digit] += 1
    
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1
    
    for i in range(n):
        arr[i] = output[i]

# Time: O(d × (n + k)) where d is digits, Space: O(n + k)
# Good for: Large numbers, fixed-width integers
```

## When to Use Each Algorithm

### Use Bubble/Insertion Sort when:
- Dataset is very small (< 10 elements)
- Data is nearly sorted
- Need simple, easy-to-understand code

### Use Merge Sort when:
- Need stable sort
- Need guaranteed O(n log n)
- Sorting linked lists
- Can afford extra space

### Use Quick Sort when:
- Average case is more important than worst case
- Need in-place sorting
- Good cache performance matters

### Use Heap Sort when:
- Need guaranteed O(n log n)
- Can't afford extra space
- Don't need stable sort

### Use Counting/Radix Sort when:
- Sorting integers with limited range
- Need O(n) time complexity

## Real-World Applications

### 1. E-commerce
Sort products by price, rating, popularity.

### 2. Databases
Index creation, query optimization.

### 3. Search Engines
Rank search results by relevance.

### 4. Operating Systems
Process scheduling, memory management.

### 5. Graphics
Z-buffer sorting for rendering.

## Practice Problems

Each problem is organized in its own directory containing:
- `problemN.md` - Problem description and examples
- `problemN.py` - Python starter file with function stubs and comments
- `test_problemN.py` - Pytest test file for validation

Navigate to each Problem directory to access the files:

- [Problem 1](./problem-1/problem1.md)
- [Problem 2](./problem-2/problem2.md)
- [Problem 3](./problem-3/problem3.md)
- [Problem 4](./problem-4/problem4.md)
- [Problem 5](./problem-5/problem5.md)
- [Problem 6](./problem-6/problem6.md)

## Next Steps

After sorting, explore [Searching Algorithms](../searching-algorithms/) to find elements efficiently!

---

💡 **Pro Tip**: For most general-purpose sorting, use built-in sort functions (like Python's `sorted()` or `list.sort()`). They typically use Timsort, an optimized hybrid of merge sort and insertion sort!
