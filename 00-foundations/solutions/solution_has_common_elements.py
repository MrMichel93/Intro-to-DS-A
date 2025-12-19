"""
Solution: Check for Common Elements - Optimization Challenge (Challenge 6)

Problem: Optimize an O(n × m) algorithm to O(n + m) using hash sets.

This solution demonstrates how choosing the right data structure dramatically
improves algorithm efficiency.
"""


def has_common_elements_slow(arr1, arr2):
    """
    INEFFICIENT VERSION: Check if two arrays share common elements.
    
    Approach:
    ---------
    Nested loop approach - for each element in arr1, check every element
    in arr2. This is the brute force solution that beginners often write.
    
    Why it's slow:
    - Must potentially compare every pair of elements
    - No optimization or early termination (except on finding match)
    
    Args:
        arr1: First array
        arr2: Second array
        
    Returns:
        Boolean: True if any common elements exist
    
    Time Complexity: O(n × m)
    -----------------
    - Outer loop: n iterations (arr1)
    - Inner loop: m iterations (arr2) per outer iteration
    - Total comparisons: n × m
    - Example: n=1000, m=1000 → 1,000,000 comparisons!
    
    Space Complexity: O(1)
    ------------------
    - No additional data structures
    - Only loop variables
    
    Examples:
    ---------
    >>> has_common_elements_slow([1, 2, 3], [4, 5, 6])
    False
    >>> has_common_elements_slow([1, 2, 3], [3, 4, 5])
    True
    """
    # Nested loops - the source of O(n × m) complexity
    for element1 in arr1:           # O(n) iterations
        for element2 in arr2:       # O(m) iterations each time
            if element1 == element2:
                return True         # Early exit on first match
    
    return False


def has_common_elements_fast(arr1, arr2):
    """
    OPTIMIZED VERSION: Check if two arrays share common elements using hash set.
    
    Approach:
    ---------
    Convert one array to a hash set (O(n)), then check if any element from
    the second array exists in that set (O(m) with O(1) lookups).
    
    Key Optimization:
    - Hash set provides O(1) average-case lookup
    - Replaces O(m) inner loop with O(1) lookup
    - Transforms O(n × m) to O(n + m)
    
    Why hash sets are powerful:
    - Hash function maps values to array indices
    - Direct memory access like arrays, but for arbitrary keys
    - Average case O(1) for insert, lookup, delete
    
    Args:
        arr1: First array
        arr2: Second array
        
    Returns:
        Boolean: True if any common elements exist
    
    Time Complexity: O(n + m)
    -----------------
    - Create set from arr1: O(n)
    - Check each arr2 element: O(m) with O(1) lookups
    - Total: O(n) + O(m) = O(n + m)
    
    Space Complexity: O(n)
    ------------------
    - Hash set stores arr1 elements: O(n)
    - Could optimize to use smaller array
    
    Performance Gain:
    - For n=1000, m=1000: 
      * Slow: 1,000,000 operations
      * Fast: 2,000 operations
      * 500x speedup!
    
    Examples:
    ---------
    >>> has_common_elements_fast([1, 2, 3], [4, 5, 6])
    False
    >>> has_common_elements_fast([1, 2, 3], [3, 4, 5])
    True
    """
    # Edge cases: if either array is empty, no common elements possible
    if not arr1 or not arr2:
        return False
    
    # Convert first array to set for O(1) lookups
    # This is the key optimization!
    set1 = set(arr1)  # O(n) time, O(n) space
    
    # Check each element of second array
    for element in arr2:  # O(m) iterations
        if element in set1:  # O(1) average-case lookup
            return True  # Found common element!
    
    return False


# Alternative Solution 1: Using set intersection (most Pythonic)
def has_common_elements_pythonic(arr1, arr2):
    """
    Most Pythonic version using set intersection.
    
    Time Complexity: O(n + m)
    Space Complexity: O(n + m)
    
    Clearest and most readable, leverages Python's built-in operations.
    """
    if not arr1 or not arr2:
        return False
    
    # Set intersection finds common elements
    return bool(set(arr1) & set(arr2))
    
    # Alternative ways to write the same thing:
    # return len(set(arr1) & set(arr2)) > 0
    # return len(set(arr1).intersection(set(arr2))) > 0


# Alternative Solution 2: Optimize for smaller array
def has_common_elements_optimized(arr1, arr2):
    """
    Optimized version that converts smaller array to set.
    
    Time Complexity: O(n + m)
    Space Complexity: O(min(n, m))
    
    Reduces space usage by choosing smaller array for set conversion.
    """
    if not arr1 or not arr2:
        return False
    
    # Use smaller array for the set to minimize space
    if len(arr1) > len(arr2):
        arr1, arr2 = arr2, arr1  # Swap so arr1 is smaller
    
    set1 = set(arr1)
    
    for element in arr2:
        if element in set1:
            return True
    
    return False


# Alternative Solution 3: Early termination with sorting (different tradeoff)
def has_common_elements_sorting(arr1, arr2):
    """
    Alternative approach using sorting with two pointers.
    
    Time Complexity: O(n log n + m log m)
    Space Complexity: O(1) if sorting in-place, O(n + m) otherwise
    
    Good when:
    - Arrays are already sorted or nearly sorted
    - Cannot use O(n) extra space for hash set
    - Need to minimize memory allocation
    """
    if not arr1 or not arr2:
        return False
    
    # Sort both arrays
    sorted1 = sorted(arr1)  # O(n log n)
    sorted2 = sorted(arr2)  # O(m log m)
    
    # Two-pointer technique
    i, j = 0, 0
    
    while i < len(sorted1) and j < len(sorted2):
        if sorted1[i] == sorted2[j]:
            return True  # Found common element
        elif sorted1[i] < sorted2[j]:
            i += 1  # Advance pointer in first array
        else:
            j += 1  # Advance pointer in second array
    
    return False


# Performance comparison function
def compare_performance(arr1, arr2):
    """
    Compare performance of slow vs fast implementation.
    """
    n, m = len(arr1), len(arr2)
    
    print(f"Array 1 size: {n}")
    print(f"Array 2 size: {m}")
    print()
    
    # Slow version analysis
    slow_ops = n * m
    print("Slow Version (Nested Loops):")
    print(f"  Time: O(n × m) = O({n} × {m}) = {slow_ops:,} operations")
    print(f"  Space: O(1)")
    print()
    
    # Fast version analysis
    fast_ops = n + m
    print("Fast Version (Hash Set):")
    print(f"  Time: O(n + m) = O({n} + {m}) = {fast_ops:,} operations")
    print(f"  Space: O(n) = O({n}) = {n:,} memory units")
    print()
    
    # Speedup calculation
    if fast_ops > 0:
        speedup = slow_ops / fast_ops
        print(f"Speedup: {speedup:.1f}x faster!")
        print()
    
    # Actual results
    result_slow = has_common_elements_slow(arr1, arr2)
    result_fast = has_common_elements_fast(arr1, arr2)
    
    print(f"Result: {result_fast}")
    print(f"Both methods agree: {result_slow == result_fast}")


# Test cases
if __name__ == "__main__":
    print("=== Optimization Challenge: O(n×m) to O(n+m) ===\n")
    
    # Test case 1: No common elements
    print("Test 1: No common elements")
    arr1, arr2 = [1, 2, 3], [4, 5, 6]
    compare_performance(arr1, arr2)
    print("-" * 60)
    
    # Test case 2: Common element exists
    print("\nTest 2: Common element exists")
    arr1, arr2 = [1, 2, 3], [3, 4, 5]
    compare_performance(arr1, arr2)
    print("-" * 60)
    
    # Test case 3: Empty arrays
    print("\nTest 3: Edge case - empty array")
    arr1, arr2 = [], [1, 2, 3]
    result = has_common_elements_fast(arr1, arr2)
    print(f"Empty array case: {result}")  # False
    print("-" * 60)
    
    # Test case 4: Large arrays (demonstrates performance difference)
    print("\nTest 4: Large arrays (performance demonstration)")
    arr1 = list(range(1000))
    arr2 = list(range(500, 1500))
    compare_performance(arr1, arr2)
    print("-" * 60)
    
    # Compare all approaches
    print("\n=== Comparing All Approaches ===")
    test_arr1 = [1, 2, 3, 4, 5]
    test_arr2 = [6, 7, 8, 4, 9]
    
    print(f"Arrays: {test_arr1} and {test_arr2}\n")
    print(f"Slow (nested):      {has_common_elements_slow(test_arr1, test_arr2)}")
    print(f"Fast (hash set):    {has_common_elements_fast(test_arr1, test_arr2)}")
    print(f"Pythonic (set &):   {has_common_elements_pythonic(test_arr1, test_arr2)}")
    print(f"Optimized (min):    {has_common_elements_optimized(test_arr1, test_arr2)}")
    print(f"Sorting (2-ptr):    {has_common_elements_sorting(test_arr1, test_arr2)}")
    
    # Key insights
    print("\n" + "=" * 60)
    print("=== KEY INSIGHTS ===")
    print("=" * 60)
    print("\n1. DATA STRUCTURE CHOICE MATTERS:")
    print("   - Wrong: Nested loops → O(n × m)")
    print("   - Right: Hash set → O(n + m)")
    print("   - Same problem, 100x-1000x difference!")
    
    print("\n2. HASH SETS PROVIDE O(1) LOOKUP:")
    print("   - Arrays: O(n) to search")
    print("   - Hash sets: O(1) average case")
    print("   - This single property changes everything!")
    
    print("\n3. SPACE-TIME TRADEOFF:")
    print("   - Slow version: O(1) space, O(n×m) time")
    print("   - Fast version: O(n) space, O(n+m) time")
    print("   - Trading memory for speed is often worth it!")
    
    print("\n4. REAL-WORLD IMPACT:")
    print("   - Small arrays (n=10): 100 ops → 20 ops (5x faster)")
    print("   - Medium arrays (n=1000): 1M ops → 2K ops (500x faster)")
    print("   - Large arrays (n=100K): 10B ops → 200K ops (50,000x faster!)")
    print("   - At scale, wrong algorithm = system failure")
    
    print("\n5. WHEN TO USE EACH:")
    print("   - Hash set: Default choice for most cases")
    print("   - Sorting: When arrays already sorted or space is critical")
    print("   - Nested loops: Only for tiny arrays or when memory is extremely limited")
