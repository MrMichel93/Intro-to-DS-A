# Array Operations Visualizations

Visual representations of common array operations to help you understand how they work.

## Array Structure

```
Array in Memory:
┌────────┬────────┬────────┬────────┬────────┐
│   10   │   20   │   30   │   40   │   50   │
└────────┴────────┴────────┴────────┴────────┘
    0        1        2        3        4      ← Indices

Direct memory addresses:
1000    1004    1008    1012    1016           ← Memory locations
                                                  (each int: 4 bytes)
```

## Access Operation - O(1)

```
Access array[2]:

Step 1: Calculate address
        base_address + (index × element_size)
        1000 + (2 × 4) = 1008

Step 2: Jump directly to location
┌────────┬────────┬────────┬────────┬────────┐
│   10   │   20   │ → 30 ← │   40   │   50   │
└────────┴────────┴────────┴────────┴────────┘
                      ↑
                   Found in 1 step!
                   
Result: 30 (constant time, regardless of array size)
```

## Search Operation - O(n)

```
Find value 40 in array:

Step 1: Check index 0
┌────────┬────────┬────────┬────────┬────────┐
│ → 10   │   20   │   30   │   40   │   50   │
└────────┴────────┴────────┴────────┴────────┘
  10 ≠ 40, continue...

Step 2: Check index 1
┌────────┬────────┬────────┬────────┬────────┐
│   10   │ → 20   │   30   │   40   │   50   │
└────────┴────────┴────────┴────────┴────────┘
  20 ≠ 40, continue...

Step 3: Check index 2
┌────────┬────────┬────────┬────────┬────────┐
│   10   │   20   │ → 30   │   40   │   50   │
└────────┴────────┴────────┴────────┴────────┘
  30 ≠ 40, continue...

Step 4: Check index 3
┌────────┬────────┬────────┬────────┬────────┐
│   10   │   20   │   30   │ → 40 ← │   50   │
└────────┴────────┴────────┴────────┴────────┘
  40 = 40, found at index 3!

Worst case: Must check every element
```

## Insert at End - O(1) with capacity

```
Insert 60 at end (when space available):

Before:
┌────────┬────────┬────────┬────────┬────────┬────────┐
│   10   │   20   │   30   │   40   │   50   │ empty  │
└────────┴────────┴────────┴────────┴────────┴────────┘
    0        1        2        3        4        5
                                         ↑
                                      length=5

After:
┌────────┬────────┬────────┬────────┬────────┬────────┐
│   10   │   20   │   30   │   40   │   50   │   60   │
└────────┴────────┴────────┴────────┴────────┴────────┘
    0        1        2        3        4        5
                                                  ↑
                                              length=6

Single operation: O(1)
```

## Insert at Beginning - O(n)

```
Insert 5 at beginning:

Before:
┌────────┬────────┬────────┬────────┬────────┐
│   10   │   20   │   30   │   40   │   50   │
└────────┴────────┴────────┴────────┴────────┘
    0        1        2        3        4

Step 1: Shift all elements right
┌────────┬────────┬────────┬────────┬────────┬────────┐
│ empty  │   10   │   20   │   30   │   40   │   50   │
└────────┴────────┴────────┴────────┴────────┴────────┘
           ←────────────────────────────────────
           Shift each element (5 operations)

Step 2: Insert new element
┌────────┬────────┬────────┬────────┬────────┬────────┐
│    5   │   10   │   20   │   30   │   40   │   50   │
└────────┴────────┴────────┴────────┴────────┴────────┘
    ↑
 Insert here

Total: n operations for n elements
```

## Insert in Middle - O(n)

```
Insert 25 at index 2:

Before:
┌────────┬────────┬────────┬────────┬────────┐
│   10   │   20   │   30   │   40   │   50   │
└────────┴────────┴────────┴────────┴────────┘
    0        1        2        3        4
                      ↑
                 Insert here

Step 1: Shift elements from index 2 onwards
┌────────┬────────┬────────┬────────┬────────┬────────┐
│   10   │   20   │ empty  │   30   │   40   │   50   │
└────────┴────────┴────────┴────────┴────────┴────────┘
                              ←─────────────────
                              Shift right (3 operations)

Step 2: Insert new element
┌────────┬────────┬────────┬────────┬────────┬────────┐
│   10   │   20   │   25   │   30   │   40   │   50   │
└────────┴────────┴────────┴────────┴────────┴────────┘
                      ↑
                 Inserted!

Average: n/2 operations = O(n)
```

## Delete from Array - O(n)

```
Delete element at index 2:

Before:
┌────────┬────────┬────────┬────────┬────────┐
│   10   │   20   │   30   │   40   │   50   │
└────────┴────────┴────────┴────────┴────────┘
    0        1        2        3        4
                      ↑
                  Delete this

Step 1: Remove element
┌────────┬────────┬────────┬────────┬────────┐
│   10   │   20   │ empty  │   40   │   50   │
└────────┴────────┴────────┴────────┴────────┘

Step 2: Shift remaining elements left
┌────────┬────────┬────────┬────────┬────────┐
│   10   │   20   │   40   │   50   │ empty  │
└────────┴────────┴────────┴────────┴────────┘
                   ──────────→
                   Shift left (2 operations)

After:
┌────────┬────────┬────────┬────────┐
│   10   │   20   │   40   │   50   │
└────────┴────────┴────────┴────────┘
    0        1        2        3

Must shift all elements after deleted position
```

## 2D Arrays (Matrices)

```
2D Array Visualization:

Logical View:
     Column 0  Column 1  Column 2
Row 0   [1]      [2]      [3]
Row 1   [4]      [5]      [6]
Row 2   [7]      [8]      [9]

Access matrix[1][2]:
- First dimension: row 1 → [4, 5, 6]
- Second dimension: column 2 → 6

Memory Layout (row-major):
[1][2][3][4][5][6][7][8][9]
 ↑       ↑       ↑
Row 0   Row 1   Row 2

Still O(1) access!
Address = base + (row × num_cols + col) × element_size
```

## Dynamic Arrays (Python Lists)

```
Python lists grow automatically:

Initial capacity = 4:
┌────────┬────────┬────────┬────────┐
│   10   │   20   │   30   │ empty  │
└────────┴────────┴────────┴────────┘

Append 40:
┌────────┬────────┬────────┬────────┐
│   10   │   20   │   30   │   40   │  ← Full!
└────────┴────────┴────────┴────────┘

Append 50 (triggers resize):

Step 1: Allocate new array (double capacity)
┌────────┬────────┬────────┬────────┬────────┬────────┬────────┬────────┐
│ empty  │ empty  │ empty  │ empty  │ empty  │ empty  │ empty  │ empty  │
└────────┴────────┴────────┴────────┴────────┴────────┴────────┴────────┘

Step 2: Copy all elements
┌────────┬────────┬────────┬────────┬────────┬────────┬────────┬────────┐
│   10   │   20   │   30   │   40   │ empty  │ empty  │ empty  │ empty  │
└────────┴────────┴────────┴────────┴────────┴────────┴────────┴────────┘

Step 3: Add new element
┌────────┬────────┬────────┬────────┬────────┬────────┬────────┬────────┐
│   10   │   20   │   30   │   40   │   50   │ empty  │ empty  │ empty  │
└────────┴────────┴────────┴────────┴────────┴────────┴────────┴────────┘

Amortized O(1) - occasional O(n) when resizing
```

## Key Takeaways

✅ **Access by index**: O(1) - Just jump to memory location  
⚠️ **Search**: O(n) - Must check each element  
⚠️ **Insert/Delete**: O(n) - Must shift elements  
✅ **Space efficient**: No extra pointers needed  

Arrays are best when:
- You need fast random access
- Size is known or rarely changes
- Memory is contiguous (cache-friendly)
