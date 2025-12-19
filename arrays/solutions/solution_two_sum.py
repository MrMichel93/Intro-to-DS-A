"""
Solution: Two Sum Problem (Challenge 1)

Problem: Find two numbers in an array that add up to a target sum.

This is one of the most famous interview problems and demonstrates the power
of hash maps for optimization.
"""


def two_sum_brute_force(nums, target):
    """
    BRUTE FORCE APPROACH: Check every pair of numbers.
    
    Approach:
    ---------
    Use nested loops to try every possible pair of indices.
    For each pair (i, j), check if nums[i] + nums[j] == target.
    
    Args:
        nums: List of integers
        target: Target sum to find
        
    Returns:
        List containing two indices [i, j] where nums[i] + nums[j] == target
    
    Time Complexity: O(n²)
    -----------------
    - Outer loop: n iterations
    - Inner loop: up to n-1 iterations
    - Total: n(n-1)/2 ≈ n²/2 = O(n²)
    
    Space Complexity: O(1)
    ------------------
    - Only stores loop variables and result
    
    Examples:
    ---------
    >>> two_sum_brute_force([2, 7, 11, 15], 9)
    [0, 1]
    >>> two_sum_brute_force([3, 2, 4], 6)
    [1, 2]
    """
    n = len(nums)
    
    # Try every pair
    for i in range(n):
        for j in range(i + 1, n):  # Start from i+1 to avoid using same element twice
            if nums[i] + nums[j] == target:
                return [i, j]
    
    # No solution found (problem guarantees solution exists)
    return []


def two_sum_hash_map(nums, target):
    """
    OPTIMIZED APPROACH: Use hash map for O(1) complement lookups.
    
    Approach:
    ---------
    For each number, calculate its complement (target - number).
    If the complement exists in our hash map, we found the answer!
    Otherwise, store the current number with its index for future lookups.
    
    Key Insight:
    If we've seen the complement before, then:
    - nums[past_index] + nums[current_index] = target
    
    Args:
        nums: List of integers
        target: Target sum to find
        
    Returns:
        List containing two indices [i, j] where nums[i] + nums[j] == target
    
    Time Complexity: O(n)
    -----------------
    - Single pass through array: n iterations
    - Hash map lookup: O(1) average case
    - Hash map insertion: O(1) average case
    - Total: O(n)
    
    Space Complexity: O(n)
    ------------------
    - Hash map stores up to n elements
    - Worst case: store all elements before finding answer
    
    Why This Is Better:
    -------------------
    Instead of checking every pair (O(n²)), we check each element once (O(n))
    by using a hash map to "remember" what we've seen.
    
    Trade-off: We use O(n) extra space to achieve O(n) time.
    
    Examples:
    ---------
    >>> two_sum_hash_map([2, 7, 11, 15], 9)
    [0, 1]
    >>> two_sum_hash_map([3, 2, 4], 6)
    [1, 2]
    >>> two_sum_hash_map([3, 3], 6)
    [0, 1]
    """
    # Dictionary to store: {number: index}
    seen = {}
    
    for i, num in enumerate(nums):
        # Calculate what we need to reach target
        complement = target - num
        
        # Check if we've seen the complement before
        if complement in seen:
            # Found it! Return the pair
            return [seen[complement], i]
        
        # Haven't found complement yet, store current number
        seen[num] = i
    
    # No solution found (problem guarantees solution exists)
    return []


def two_sum_sorted(nums, target):
    """
    ALTERNATIVE APPROACH: Two pointers on sorted array.
    
    Approach:
    ---------
    If we sort the array first, we can use two pointers:
    - One at start (smallest number)
    - One at end (largest number)
    
    If sum is too small, move left pointer right (increase sum).
    If sum is too large, move right pointer left (decrease sum).
    
    CAVEAT: Sorting changes indices, so we need to track original positions!
    
    Args:
        nums: List of integers
        target: Target sum to find
        
    Returns:
        List containing two indices [i, j] from ORIGINAL array
    
    Time Complexity: O(n log n)
    -----------------
    - Sorting: O(n log n)
    - Two-pointer scan: O(n)
    - Total: O(n log n) (dominated by sorting)
    
    Space Complexity: O(n)
    ------------------
    - Need to store (value, original_index) pairs
    - Sorting creates new array
    
    When to Use This:
    -----------------
    - If array is already sorted (then it's O(n) time!)
    - If you need to find multiple pairs
    - When you want to avoid hash map (memory constrained)
    
    Examples:
    ---------
    >>> two_sum_sorted([2, 7, 11, 15], 9)
    [0, 1]
    >>> two_sum_sorted([3, 2, 4], 6)
    [1, 2]
    """
    # Store (value, original_index) pairs
    indexed_nums = [(num, i) for i, num in enumerate(nums)]
    
    # Sort by value
    indexed_nums.sort()
    
    # Two pointers
    left = 0
    right = len(indexed_nums) - 1
    
    while left < right:
        current_sum = indexed_nums[left][0] + indexed_nums[right][0]
        
        if current_sum == target:
            # Found it! Return original indices
            idx1 = indexed_nums[left][1]
            idx2 = indexed_nums[right][1]
            # Return in sorted order of indices
            return [min(idx1, idx2), max(idx1, idx2)]
        elif current_sum < target:
            # Sum too small, need larger numbers
            left += 1
        else:
            # Sum too large, need smaller numbers
            right -= 1
    
    # No solution found
    return []


# Performance comparison
def compare_approaches(nums, target):
    """
    Compare all three approaches and their characteristics.
    """
    n = len(nums)
    
    print(f"Array: {nums}")
    print(f"Target: {target}")
    print(f"Size: {n}\n")
    
    print("=" * 60)
    print("APPROACH COMPARISON")
    print("=" * 60)
    
    approaches = [
        {
            "name": "Brute Force (Nested Loops)",
            "time": f"O(n²) = O({n}²) ≈ {n*n} operations",
            "space": "O(1)",
            "best_for": "Tiny arrays (n < 10)",
            "function": two_sum_brute_force
        },
        {
            "name": "Hash Map (Optimal)",
            "time": f"O(n) = O({n}) = {n} operations",
            "space": "O(n)",
            "best_for": "Most cases (default choice)",
            "function": two_sum_hash_map
        },
        {
            "name": "Two Pointers (Sorted)",
            "time": f"O(n log n) ≈ {n * (n.bit_length() if n > 0 else 0)} operations",
            "space": "O(n)",
            "best_for": "Already sorted input",
            "function": two_sum_sorted
        }
    ]
    
    for i, approach in enumerate(approaches, 1):
        print(f"\n{i}. {approach['name']}")
        print(f"   Time:     {approach['time']}")
        print(f"   Space:    {approach['space']}")
        print(f"   Best for: {approach['best_for']}")
        print(f"   Result:   {approach['function'](nums.copy(), target)}")
    
    # Performance analysis
    if n >= 10:
        speedup = (n * n) / n
        print(f"\n{'=' * 60}")
        print(f"For n={n}:")
        print(f"  Brute force: {n*n:,} operations")
        print(f"  Hash map:    {n:,} operations")
        print(f"  Speedup:     {speedup:.0f}x faster!")


# Test cases
if __name__ == "__main__":
    print("=" * 70)
    print("TWO SUM PROBLEM - CHALLENGE 1 SOLUTIONS")
    print("=" * 70)
    
    # Test case 1
    print("\nTest 1: Basic case")
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Hash Map Result: {two_sum_hash_map(nums1, target1)}")
    print(f"Expected: [0, 1]")
    
    # Test case 2
    print("\nTest 2: Solution not at start")
    nums2 = [3, 2, 4]
    target2 = 6
    print(f"Input: nums = {nums2}, target = {target2}")
    print(f"Hash Map Result: {two_sum_hash_map(nums2, target2)}")
    print(f"Expected: [1, 2]")
    
    # Test case 3
    print("\nTest 3: Duplicate numbers")
    nums3 = [3, 3]
    target3 = 6
    print(f"Input: nums = {nums3}, target = {target3}")
    print(f"Hash Map Result: {two_sum_hash_map(nums3, target3)}")
    print(f"Expected: [0, 1]")
    
    # Test case 4: Negative numbers
    print("\nTest 4: Negative numbers")
    nums4 = [-1, -2, -3, -4, -5]
    target4 = -8
    print(f"Input: nums = {nums4}, target = {target4}")
    print(f"Hash Map Result: {two_sum_hash_map(nums4, target4)}")
    print(f"Expected: [2, 4] (since -3 + -5 = -8)")
    
    # Performance comparison
    print("\n" + "=" * 70)
    compare_approaches([2, 7, 11, 15, 20, 30], 50)
    
    # Key insights
    print("\n" + "=" * 70)
    print("KEY INSIGHTS")
    print("=" * 70)
    print("""
1. HASH MAP IS THE STANDARD SOLUTION
   - O(n) time with single pass
   - O(n) space for hash map
   - Most efficient for general case

2. COMPLEMENT PATTERN
   - For each number x, look for (target - x)
   - Hash map provides O(1) complement lookup
   - Store as you go to handle all cases

3. SPACE-TIME TRADEOFF
   - Brute force: O(1) space, O(n²) time
   - Hash map: O(n) space, O(n) time
   - Trading memory for speed is usually worth it!

4. REAL-WORLD APPLICATIONS
   - Cryptocurrency trading: Find coin pairs for target portfolio value
   - Budgeting apps: Find expense pairs that sum to spending limit
   - Chemistry: Find molecules that combine to target molecular weight
   - Gaming: Find item combinations for exact cost

5. COMMON VARIATIONS
   - Three Sum: Extend to find three numbers (O(n²) with sorting)
   - K Sum: Generalize to k numbers
   - Two Sum II: Input is sorted (use two pointers, O(n) time, O(1) space)
   - Two Sum with multiplicity: Count all pairs (not just indices)
    """)
