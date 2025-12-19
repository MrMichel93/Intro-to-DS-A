# Arrays Module - Practice Challenges

These challenges will help you master array operations, including searching, manipulation, two-pointer techniques, and sliding window algorithms.

## Challenge 1: Two Sum Problem (Beginner)

**Difficulty:** Beginner 🟢

**Objective**: Find two numbers in an array that add up to a target sum.

**Expected Time Complexity**: O(n) with hash map approach
**Expected Space Complexity**: O(n) for hash map

**Real-World Use Case**: E-commerce platforms like Amazon use variations of this algorithm in their "Frequently Bought Together" recommendations. By analyzing transaction data, they find pairs of items that customers often purchase together (where the "sum" represents shopping cart patterns or price combinations).

### Problem Statement

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers that add up to `target`. You may assume that each input has exactly one solution, and you cannot use the same element twice.

**Requirements**:
- Return the indices as a list [index1, index2]
- You cannot use the same element twice
- The solution must exist (guaranteed by problem)

### Examples

**Example 1**:
```python
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9
```

**Example 2**:
```python
Input: nums = [3, 2, 4], target = 6
Output: [1, 2]
Explanation: nums[1] + nums[2] = 2 + 4 = 6
```

**Example 3**:
```python
Input: nums = [3, 3], target = 6
Output: [0, 1]
Explanation: nums[0] + nums[1] = 3 + 3 = 6
```

### Constraints

- 2 ≤ nums.length ≤ 10⁴
- -10⁹ ≤ nums[i] ≤ 10⁹
- -10⁹ ≤ target ≤ 10⁹
- Only one valid answer exists

### Hints

<details>
<summary>Hint 1</summary>
For each number, think about what its complement would be (target - current number). Have you seen that complement before?
</details>

<details>
<summary>Hint 2</summary>
A hash map can store numbers you've seen along with their indices, allowing O(1) lookup time.
</details>

<details>
<summary>Hint 3</summary>
You can solve this in a single pass through the array by checking if the complement exists in your hash map before adding the current number.
</details>

---

## Challenge 2: Remove Duplicates from Sorted Array (Beginner)

**Difficulty:** Beginner 🟢

**Objective**: Remove duplicates from a sorted array in-place.

**Expected Time Complexity**: O(n)
**Expected Space Complexity**: O(1)

**Real-World Use Case**: Database systems use similar algorithms when implementing the SQL DISTINCT keyword. When returning unique results from a sorted index, the database efficiently removes duplicates in-place without creating a new result set, saving memory for large query results.

### Problem Statement

Given a sorted array `nums`, remove the duplicates in-place such that each element appears only once and returns the new length. Do not allocate extra space for another array; you must modify the input array in-place with O(1) extra memory.

**Requirements**:
- Modify the array in-place
- Return the new length k
- First k elements should contain unique values in sorted order
- Elements beyond position k don't matter

### Examples

**Example 1**:
```python
Input: nums = [1, 1, 2]
Output: 2, nums = [1, 2, _]
Explanation: Your function should return length 2, with the first two elements being 1 and 2.
```

**Example 2**:
```python
Input: nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
Output: 5, nums = [0, 1, 2, 3, 4, _, _, _, _, _]
Explanation: First five elements are unique values in sorted order.
```

**Example 3**:
```python
Input: nums = [1, 2, 3, 4, 5]
Output: 5, nums = [1, 2, 3, 4, 5]
Explanation: No duplicates, all elements remain.
```

### Constraints

- 0 ≤ nums.length ≤ 3 × 10⁴
- -100 ≤ nums[i] ≤ 100
- `nums` is sorted in non-decreasing order

### Hints

<details>
<summary>Hint 1</summary>
Since the array is sorted, duplicates will always be adjacent. You only need to compare consecutive elements.
</details>

<details>
<summary>Hint 2</summary>
Use two pointers: one for reading through the array, and one for writing unique elements.
</details>

<details>
<summary>Hint 3</summary>
The "write" pointer only advances when you find a new unique element. The "read" pointer always advances.
</details>

---

## Challenge 3: Product of Array Except Self (Intermediate)

**Difficulty:** Intermediate 🟡

**Objective**: Calculate the product of all elements except the current one without using division.

**Expected Time Complexity**: O(n)
**Expected Space Complexity**: O(1) (output array doesn't count)

**Real-World Use Case**: Financial analytics platforms calculate relative performance metrics. For example, a stock trading dashboard might show each stock's return compared to the average of all other stocks in a portfolio. Computing "product of all except self" efficiently is crucial when analyzing thousands of securities in real-time.

### Problem Statement

Given an integer array `nums`, return an array `output` where `output[i]` equals the product of all elements of `nums` except `nums[i]`. You must solve it without using division and in O(n) time.

**Requirements**:
- Cannot use division operator
- Must run in O(n) time
- Output array doesn't count as extra space

### Examples

**Example 1**:
```python
Input: nums = [1, 2, 3, 4]
Output: [24, 12, 8, 6]
Explanation:
- output[0] = 2 * 3 * 4 = 24
- output[1] = 1 * 3 * 4 = 12
- output[2] = 1 * 2 * 4 = 8
- output[3] = 1 * 2 * 3 = 6
```

**Example 2**:
```python
Input: nums = [-1, 1, 0, -3, 3]
Output: [0, 0, 9, 0, 0]
Explanation:
- output[0] = 1 * 0 * -3 * 3 = 0
- output[1] = -1 * 0 * -3 * 3 = 0
- output[2] = -1 * 1 * -3 * 3 = 9
- output[3] = -1 * 1 * 0 * 3 = 0
- output[4] = -1 * 1 * 0 * -3 = 0
```

**Example 3**:
```python
Input: nums = [2, 3, 4, 5]
Output: [60, 40, 30, 24]
```

### Constraints

- 2 ≤ nums.length ≤ 10⁵
- -30 ≤ nums[i] ≤ 30
- The product of any prefix or suffix is guaranteed to fit in a 32-bit integer

### Hints

<details>
<summary>Hint 1</summary>
Think about the product at position i as: (product of all elements to the left) × (product of all elements to the right).
</details>

<details>
<summary>Hint 2</summary>
You can calculate prefix products (left to right) and suffix products (right to left) in separate passes.
</details>

<details>
<summary>Hint 3</summary>
To achieve O(1) space, compute the output array with prefix products first, then multiply by suffix products in a second pass without storing the suffix array.
</details>

---

## Challenge 4: Container With Most Water (Intermediate)

**Difficulty:** Intermediate 🟡

**Objective**: Find two lines that together with the x-axis form a container that holds the most water.

**Expected Time Complexity**: O(n)
**Expected Space Complexity**: O(1)

**Real-World Use Case**: Civil engineers use similar algorithms to optimize water reservoir designs. Given varying terrain heights, they need to determine where to place dam walls to maximize water storage capacity while minimizing construction costs. The two-pointer technique efficiently finds optimal placement positions.

### Problem Statement

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i-th` line are `(i, 0)` and `(i, height[i])`. Find two lines that together with the x-axis form a container that contains the most water. Return the maximum amount of water a container can store.

**Requirements**:
- Calculate area as: width × min(height1, height2)
- Find the maximum possible area
- You cannot slant the container

### Examples

**Example 1**:
```python
Input: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
Output: 49
Explanation: Lines at indices 1 and 8 form a container.
- Width = 8 - 1 = 7
- Height = min(8, 7) = 7
- Area = 7 × 7 = 49
```

**Example 2**:
```python
Input: height = [1, 1]
Output: 1
Explanation: Only two lines, area = 1 × 1 = 1
```

**Example 3**:
```python
Input: height = [4, 3, 2, 1, 4]
Output: 16
Explanation: Lines at indices 0 and 4 form container.
- Width = 4 - 0 = 4
- Height = min(4, 4) = 4
- Area = 4 × 4 = 16
```

### Constraints

- 2 ≤ height.length ≤ 10⁵
- 0 ≤ height[i] ≤ 10⁴

### Hints

<details>
<summary>Hint 1</summary>
Start with the widest container (first and last elements). This gives you the maximum possible width.
</details>

<details>
<summary>Hint 2</summary>
Use two pointers, one at each end. The area is limited by the shorter line. Which pointer should you move?
</details>

<details>
<summary>Hint 3</summary>
Always move the pointer pointing to the shorter line. Moving the taller line pointer cannot increase area since width decreases and height is already limited by the shorter line.
</details>

---

## Challenge 5: Find All Subarrays with Given Sum (Advanced)

**Difficulty:** Advanced 🔴

**Objective**: Find all contiguous subarrays that sum to a target value.

**Expected Time Complexity**: O(n)
**Expected Space Complexity**: O(n) for hash map

**Real-World Use Case**: Cybersecurity systems use subarray sum algorithms to detect anomalous network traffic patterns. By monitoring cumulative data packet sizes over time windows, they can identify specific time intervals where traffic volume matches known attack signatures or exceeds normal thresholds, triggering security alerts.

### Problem Statement

Given an array of integers `nums` and an integer `target`, find all pairs of indices `[start, end]` where the subarray `nums[start:end+1]` sums to `target`. Return all such pairs in any order.

**Requirements**:
- Find ALL subarrays (not just count)
- Return as list of [start_index, end_index] pairs
- Subarrays must be contiguous
- Empty subarrays don't count (start ≤ end)

### Examples

**Example 1**:
```python
Input: nums = [1, 2, 3, 4, 5], target = 9
Output: [[1, 3], [3, 4]]
Explanation:
- nums[1:4] = [2, 3, 4] sums to 9
- nums[3:5] = [4, 5] sums to 9
```

**Example 2**:
```python
Input: nums = [1, 1, 1], target = 2
Output: [[0, 1], [1, 2]]
Explanation:
- nums[0:2] = [1, 1] sums to 2
- nums[1:3] = [1, 1] sums to 2
```

**Example 3**:
```python
Input: nums = [1, -1, 1, -1, 1], target = 0
Output: [[0, 1], [1, 2], [2, 3], [3, 4], [0, 3], [1, 4]]
Explanation: Multiple overlapping subarrays sum to 0
```

### Constraints

- 1 ≤ nums.length ≤ 10⁴
- -10⁶ ≤ nums[i] ≤ 10⁶
- -10⁹ ≤ target ≤ 10⁹

### Hints

<details>
<summary>Hint 1</summary>
Use a prefix sum approach: if prefix_sum[j] - prefix_sum[i] = target, then the subarray from i+1 to j sums to target.
</details>

<details>
<summary>Hint 2</summary>
Store each prefix sum with all indices where it occurs using a hash map with lists as values.
</details>

<details>
<summary>Hint 3</summary>
For each position, look for prefix_sum - target in your hash map. Each occurrence represents a valid subarray ending at the current position.
</details>

---

## Challenge 6: Trapping Rain Water (Advanced)

**Difficulty:** Advanced 🔴

**Objective**: Calculate how much water can be trapped after raining given elevation map.

**Expected Time Complexity**: O(n)
**Expected Space Complexity**: O(1) with two-pointer approach

**Real-World Use Case**: Urban planning departments use similar algorithms to model stormwater drainage. Given the elevation profile of streets and terrain, civil engineers calculate where water will pool during heavy rainfall, helping them design drainage systems and prevent flooding in city infrastructure projects.

### Problem Statement

Given `n` non-negative integers representing an elevation map where the width of each bar is 1, compute how much water can be trapped after raining.

**Requirements**:
- Each bar has width 1
- Water fills spaces between bars
- Water cannot spill beyond the boundaries
- Return total water volume (sum of all trapped water)

### Examples

**Example 1**:
```python
Input: height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
Output: 6
Explanation:
Elevation map:
     █
 █   ███ █ █
_█_█_███████
Water trapped at each position:
[0,0,1,0,1,2,1,0,0,1,0,0]
Total: 6 units
```

**Example 2**:
```python
Input: height = [4, 2, 0, 3, 2, 5]
Output: 9
Explanation:
    █
█   ███
████████
Water fills: [0,2,4,1,2,0]
Total: 9 units
```

**Example 3**:
```python
Input: height = [3, 0, 2, 0, 4]
Output: 7
Explanation:
    █
█ █ █
█████
Water: [0,3,1,3,0]
Total: 7 units
```

### Constraints

- 0 ≤ height.length ≤ 2 × 10⁴
- 0 ≤ height[i] ≤ 10⁵

### Hints

<details>
<summary>Hint 1</summary>
Water trapped at position i = min(max_left_height, max_right_height) - height[i], if positive.
</details>

<details>
<summary>Hint 2</summary>
You can precompute max_left and max_right arrays in O(n) time, then calculate trapped water in a third pass.
</details>

<details>
<summary>Hint 3</summary>
For O(1) space: use two pointers from both ends. Move the pointer with the smaller max height, since that's the limiting factor for water level.
</details>

<details>
<summary>Hint 4</summary>
With two pointers, maintain max_left and max_right as you go. At each step, you know which side limits the water height, so you can calculate trapped water incrementally.
</details>

---

## Summary and Next Steps

These challenges covered:
- ✅ Hash map techniques for O(n) searching (Challenge 1)
- ✅ Two-pointer technique for in-place modification (Challenge 2)
- ✅ Prefix/suffix product patterns (Challenge 3)
- ✅ Two-pointer optimization for max area (Challenge 4)
- ✅ Prefix sum with hash maps (Challenge 5)
- ✅ Two-pointer technique for complex calculations (Challenge 6)

### Key Lessons

1. **Hash maps enable O(n) solutions** - Transform O(n²) nested loops into O(n) single passes
2. **Two pointers for in-place operations** - Modify arrays efficiently without extra space
3. **Prefix/suffix techniques** - Break complex calculations into simpler left-to-right and right-to-left passes
4. **Greedy two-pointer optimization** - Move pointers strategically based on problem constraints
5. **Prefix sums unlock subarray problems** - Convert range queries into O(1) lookups

### Ready for More?

Once you're comfortable with these challenges, explore:
- **[Linked Lists](../linked-lists/)** - Learn dynamic memory allocation
- **[Stacks](../stacks/)** - Master LIFO operations
- **[Sorting Algorithms](../sorting-algorithms/)** - Optimize array ordering

---

💡 **Remember**: Arrays are the foundation of many advanced algorithms. Master these patterns, and you'll recognize them everywhere!
