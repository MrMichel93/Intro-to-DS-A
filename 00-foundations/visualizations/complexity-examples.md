# Time Complexity Visualizations

This document provides visual representations of different time complexities to help you understand algorithm efficiency.

## O(1) - Constant Time

**Example: Accessing an array element by index**

```
Operation: array[3]

Array: [10][20][30][40][50]
Index:  0   1   2   3   4
                    ↑
                Direct access!

No matter how large the array:
- 10 elements: 1 operation
- 1,000 elements: 1 operation
- 1,000,000 elements: 1 operation
```

## O(log n) - Logarithmic Time

**Example: Binary search in a sorted array**

```
Find 37 in: [5, 15, 23, 37, 42, 58, 67, 81, 95]

Step 1: Check middle (42)
[5, 15, 23, 37, 42, 58, 67, 81, 95]
                ↑
            37 < 42, search left half

Step 2: Check middle of left half (23)
[5, 15, 23, 37]
        ↑
    37 > 23, search right

Step 3: Check middle (37)
[37]
 ↑
Found it!

Total steps: 3 for 9 elements
Doubles in size? Only adds 1 step!
```

## O(n) - Linear Time

**Example: Finding maximum value in unsorted array**

```
Find max in: [23, 7, 15, 42, 8, 31]

Step 1: max = 23  [23]  7   15  42  8   31
Step 2: max = 23   23  [7]  15  42  8   31
Step 3: max = 23   23   7  [15] 42  8   31
Step 4: max = 42   23   7   15 [42] 8   31  ← New max!
Step 5: max = 42   23   7   15  42 [8]  31
Step 6: max = 42   23   7   15  42  8  [31]

Must check every element: n operations for n elements
```

## O(n log n) - Linearithmic Time

**Example: Merge Sort**

```
Sort: [38, 27, 43, 3, 9, 82, 10]

              [38,27,43,3,9,82,10]
                     / \
           [38,27,43]   [3,9,82,10]
            /    \         /    \
       [38]  [27,43]   [3,9]  [82,10]
              /  \      / \     /  \
           [27] [43]  [3] [9] [82] [10]
              
         Merge back together (sorted):
           [27,43]      [3,9]   [10,82]
              \          /          /
           [27,38,43]  [3,9,10,82]
                  \        /
            [3,9,10,27,38,43,82]

Splits: log n levels
Merges at each level: n operations
Total: n × log n
```

## O(n²) - Quadratic Time

**Example: Bubble Sort (worst case)**

```
Sort: [5, 2, 4, 1, 3]

Pass 1: Compare each adjacent pair
[5, 2, 4, 1, 3]  → [2, 5, 4, 1, 3]  (swap 5,2)
[2, 5, 4, 1, 3]  → [2, 4, 5, 1, 3]  (swap 5,4)
[2, 4, 5, 1, 3]  → [2, 4, 1, 5, 3]  (swap 5,1)
[2, 4, 1, 5, 3]  → [2, 4, 1, 3, 5]  (swap 5,3)

Pass 2: Repeat for n-1 elements
[2, 4, 1, 3, 5]  → [2, 4, 1, 3, 5]  (no swap)
[2, 4, 1, 3, 5]  → [2, 1, 4, 3, 5]  (swap 4,1)
[2, 1, 4, 3, 5]  → [2, 1, 3, 4, 5]  (swap 4,3)

Pass 3: Continue...
[2, 1, 3, 4, 5]  → [1, 2, 3, 4, 5]  (swap 2,1)
...

For n elements: n passes × n comparisons = n²
```

## O(2ⁿ) - Exponential Time

**Example: Naive Fibonacci (recursive)**

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```

```
Computing fib(5):

                    fib(5)
                   /      \
              fib(4)      fib(3)
              /    \      /    \
          fib(3) fib(2) fib(2) fib(1)
          /  \    /  \   /  \
      fib(2) fib(1) ...  ...  ...
      /  \
  fib(1) fib(0)

Notice: Many repeated calculations!
fib(2) computed 3 times
fib(3) computed 2 times

Tree roughly doubles at each level
Height: n levels
Total nodes: ≈ 2ⁿ
```

## Comparison Chart

```
Time for different input sizes:

Algorithm    n=10    n=100    n=1,000    n=10,000
-------------------------------------------------
O(1)         1       1        1          1
O(log n)     3       7        10         13
O(n)         10      100      1,000      10,000
O(n log n)   30      700      10,000     130,000
O(n²)        100     10,000   1,000,000  100,000,000
O(2ⁿ)        1,024   ∞        ∞          ∞

∞ = Too large to compute in reasonable time
```

## Growth Rates Visualization

```
Operations (y-axis) vs Input Size (x-axis)

For n = 10:
O(1):      *
O(log n):  **
O(n):      **********
O(n log n):*****************************
O(n²):     ****************************************************
           ****************************************************
O(2ⁿ):     [Would go off the page!]

For n = 100:
O(1):      *
O(log n):  ***
O(n):      [100 stars]
O(n log n):[700 stars]
O(n²):     [10,000 stars - would fill many screens!]
O(2ⁿ):     [Impossible to show]
```

## Real-World Impact

```
Task: Process 1 million items (n = 1,000,000)
Assume: 1 operation = 1 microsecond

O(1):        1 microsecond     (instant!)
O(log n):    20 microseconds   (instant!)
O(n):        1 second          (fast)
O(n log n):  20 seconds        (acceptable)
O(n²):       11.5 days         (too slow!)
O(2ⁿ):       10²⁹⁸⁹⁸⁰ years    (never finishes!)
```

## Key Takeaways

1. **Constant factors don't matter in Big O**
   - O(2n) = O(n)
   - O(100) = O(1)

2. **Lower order terms are dropped**
   - O(n² + n) = O(n²)
   - O(n log n + n) = O(n log n)

3. **Different inputs = different variables**
   - Array of size n and m: O(n × m)
   - Not just O(n²)!

4. **Best, Average, Worst Case**
   - Quicksort: O(n log n) average, O(n²) worst
   - Always consider the worst case

---

💡 **Pro Tip**: When analyzing your code, count the nested loops:
- 1 loop: Usually O(n)
- 2 nested loops: Usually O(n²)
- 3 nested loops: Usually O(n³)
- Dividing problem in half: Usually O(log n)
