"""
Solution: Find Second Largest Element (Challenge 4)

Problem: Find the second largest element in an array in O(n) time.

This solution demonstrates efficient linear-time traversal with state tracking.
"""


def find_second_largest(arr):
    """
    Find the second largest element in an array using a single pass.
    
    Approach:
    ---------
    We maintain two variables (largest and second_largest) and update them
    as we scan through the array. This is a classic "tracking multiple states"
    pattern that appears frequently in algorithm problems.
    
    Key Insight:
    When we find a new maximum, the old maximum becomes the second largest.
    When we find a value between the maximum and second largest, it becomes
    the new second largest.
    
    Args:
        arr: List of integers
        
    Returns:
        Second largest integer or None if not enough elements
    
    Time Complexity: O(n)
    -----------------
    - Single loop through array: n iterations
    - Per iteration: 2 comparisons (worst case), 2 assignments (worst case)
    - Total operations: ~4n
    - Big-O: O(n) - linear time
    
    Space Complexity: O(1)
    ------------------
    - Only two variables: largest and second_largest
    - No additional arrays or data structures
    - Space doesn't grow with input size
    
    Why not sort? Sorting would be O(n log n), which is slower than O(n).
    
    Examples:
    ---------
    >>> find_second_largest([10, 5, 20, 8, 15])
    15
    >>> find_second_largest([3, 3, 2, 1])
    3
    >>> find_second_largest([5])
    None
    >>> find_second_largest([7, 7, 7, 7])
    7
    """
    # Edge case: need at least 2 elements
    if len(arr) < 2:
        return None
    
    # Initialize with negative infinity to handle negative numbers
    largest = second_largest = float('-inf')
    
    # Single pass through array
    for num in arr:
        if num > largest:
            # New maximum found!
            # The old maximum becomes second largest
            second_largest = largest
            largest = num
        elif num > second_largest:
            # Not larger than max, but larger than second
            # This also handles duplicates of the maximum
            second_largest = num
    
    # Handle case where all elements are the same or only one unique value
    if second_largest == float('-inf'):
        return None
    
    return second_largest


# Alternative Solution 1: Using sorting (O(n log n), less efficient)
def find_second_largest_sorting(arr):
    """
    Alternative approach using sorting.
    
    Time Complexity: O(n log n) - dominated by sorting
    Space Complexity: O(n) - sorted() creates a new array
    
    This is less efficient but simpler to understand.
    Good for small arrays or when code clarity is prioritized over performance.
    """
    if len(arr) < 2:
        return None
    
    # Sort in descending order
    sorted_arr = sorted(arr, reverse=True)
    
    # Return second element (handles duplicates by allowing same value)
    return sorted_arr[1]


# Alternative Solution 2: Find second unique largest (different semantics)
def find_second_largest_unique(arr):
    """
    Find second largest UNIQUE value (excludes duplicates of max).
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Example: [5, 5, 3, 2] returns 3 (not 5)
    Compare with main solution: [5, 5, 3, 2] returns 5
    """
    if len(arr) < 2:
        return None
    
    largest = second = float('-inf')
    
    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            # Only update if it's different from largest
            second = num
    
    return second if second != float('-inf') else None


# Alternative Solution 3: Using two-pass approach (still O(n))
def find_second_largest_two_pass(arr):
    """
    Two-pass approach: find max first, then find second.
    
    Time Complexity: O(n) - two passes = 2n = O(n)
    Space Complexity: O(1)
    
    Easier to understand but makes two passes instead of one.
    """
    if len(arr) < 2:
        return None
    
    # First pass: find maximum
    largest = max(arr)
    
    # Second pass: find largest value that's not the maximum
    second_largest = float('-inf')
    for num in arr:
        if num < largest and num > second_largest:
            second_largest = num
        elif num == largest and num > second_largest:
            # Handle duplicates of maximum
            second_largest = num
    
    return second_largest if second_largest != float('-inf') else None


# Optimized Solution: Early termination for small arrays
def find_second_largest_optimized(arr):
    """
    Optimized version with early returns and input validation.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Includes optimizations for common cases.
    """
    n = len(arr)
    
    # Quick returns for edge cases
    if n < 2:
        return None
    
    if n == 2:
        # For exactly 2 elements, return the smaller (or equal)
        return min(arr)
    
    # Initialize with first two elements
    if arr[0] > arr[1]:
        largest, second_largest = arr[0], arr[1]
    else:
        largest, second_largest = arr[1], arr[0]
    
    # Process remaining elements
    for i in range(2, n):
        num = arr[i]
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
    
    return second_largest


# Test cases
if __name__ == "__main__":
    print("=== Testing find_second_largest ===\n")
    
    # Test case 1: Regular array
    test1 = [10, 5, 20, 8, 15]
    print(f"Test 1: {test1}")
    print(f"Result: {find_second_largest(test1)}")  # Expected: 15
    print()
    
    # Test case 2: Array with duplicates
    test2 = [3, 3, 2, 1]
    print(f"Test 2: {test2}")
    print(f"Result: {find_second_largest(test2)}")  # Expected: 3
    print()
    
    # Test case 3: Single element
    test3 = [5]
    print(f"Test 3: {test3}")
    print(f"Result: {find_second_largest(test3)}")  # Expected: None
    print()
    
    # Test case 4: All same elements
    test4 = [7, 7, 7, 7]
    print(f"Test 4: {test4}")
    print(f"Result: {find_second_largest(test4)}")  # Expected: 7
    print()
    
    # Test case 5: Negative numbers
    test5 = [-5, -2, -10, -1]
    print(f"Test 5: {test5}")
    print(f"Result: {find_second_largest(test5)}")  # Expected: -2
    print()
    
    # Test case 6: Two elements
    test6 = [100, 50]
    print(f"Test 6: {test6}")
    print(f"Result: {find_second_largest(test6)}")  # Expected: 50
    print()
    
    # Comparing all approaches
    print("=== Comparing Approaches ===")
    test_arr = [15, 10, 25, 8, 20]
    print(f"Test array: {test_arr}\n")
    print(f"Single-pass O(n):        {find_second_largest(test_arr)}")
    print(f"Sorting O(n log n):      {find_second_largest_sorting(test_arr)}")
    print(f"Second unique O(n):      {find_second_largest_unique(test_arr)}")
    print(f"Two-pass O(n):           {find_second_largest_two_pass(test_arr)}")
    print(f"Optimized O(n):          {find_second_largest_optimized(test_arr)}")
    
    print("\n--- Complexity Analysis ---")
    print("Time: O(n) - Single pass through array")
    print("Space: O(1) - Only two tracking variables")
    print("\nKey Insight: We can track multiple 'best' values in a single")
    print("pass by updating our tracking variables based on comparisons.")
    print("This is more efficient than sorting (O(n log n)).")
