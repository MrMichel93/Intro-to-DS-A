"""
Solution: Get Middle Element (Challenge 3)

Problem: Return the middle element of an array in O(1) time complexity.

This solution demonstrates constant-time array access through direct indexing.
"""


def get_middle_element(arr):
    """
    Return the middle element of an array in O(1) time.
    
    Approach:
    ---------
    This solution leverages the fundamental property of arrays: direct access
    by index. Since arrays store elements in contiguous memory, we can calculate
    the exact memory address of any element instantly using:
        address = base_address + (index × element_size)
    
    For the middle element:
    1. Get array length: O(1) - Python stores this as metadata
    2. Calculate middle index using integer division: O(1) - single arithmetic operation
    3. Access element at middle index: O(1) - direct memory access
    
    Args:
        arr: List of elements
        
    Returns:
        Middle element or None if array is empty
    
    Time Complexity: O(1)
    -----------------
    - len(arr): O(1) - Python lists store their length
    - Integer division (//): O(1) - single CPU instruction
    - Array indexing: O(1) - direct memory address calculation
    - Total: O(1) + O(1) + O(1) = O(1)
    
    Space Complexity: O(1)
    ------------------
    - Only stores mid_index variable: 1 integer = constant space
    - No arrays, lists, or data structures created
    - Space used doesn't grow with input size
    
    Examples:
    ---------
    >>> get_middle_element([1, 2, 3, 4, 5])
    3
    >>> get_middle_element([1, 2, 3, 4])
    3
    >>> get_middle_element([7])
    7
    >>> get_middle_element([])
    None
    """
    # Edge case: empty array
    if len(arr) == 0:
        return None
    
    # Calculate middle index
    # For odd length: exactly in the center (e.g., len=5, mid=2, arr[2])
    # For even length: right-middle element (e.g., len=4, mid=2, arr[2])
    mid_index = len(arr) // 2
    
    # Direct array access - this is why arrays are powerful!
    return arr[mid_index]


# Alternative Solution 1: Using negative indexing (still O(1))
def get_middle_element_v2(arr):
    """
    Alternative approach using Python's negative indexing.
    
    Time Complexity: O(1)
    Space Complexity: O(1)
    
    This is mathematically equivalent but uses Python's built-in
    support for negative indices to access from the end.
    """
    if len(arr) == 0:
        return None
    
    # For odd length arrays, we could also use:
    # return arr[-(len(arr) // 2 + 1)] for left-middle
    # But the standard approach is clearer
    
    return arr[len(arr) // 2]


# Alternative Solution 2: With bounds checking (defensive programming)
def get_middle_element_v3(arr):
    """
    Defensive version with explicit bounds checking.
    
    Time Complexity: O(1)
    Space Complexity: O(1)
    
    Good practice for production code where invalid input is possible.
    """
    # Validate input type
    if not isinstance(arr, (list, tuple)):
        raise TypeError(f"Expected list or tuple, got {type(arr)}")
    
    # Handle empty array
    if len(arr) == 0:
        return None
    
    # Calculate and validate index
    mid_index = len(arr) // 2
    
    # This check is redundant for our calculation, but shows defensive style
    if 0 <= mid_index < len(arr):
        return arr[mid_index]
    
    # Should never reach here with correct calculation
    return None


# Test cases
if __name__ == "__main__":
    # Test case 1: Odd-length array
    print("Test 1 (odd length):", get_middle_element([1, 2, 3, 4, 5]))  # Expected: 3
    
    # Test case 2: Even-length array
    print("Test 2 (even length):", get_middle_element([1, 2, 3, 4]))  # Expected: 3
    
    # Test case 3: Single element
    print("Test 3 (single element):", get_middle_element([7]))  # Expected: 7
    
    # Test case 4: Empty array
    print("Test 4 (empty):", get_middle_element([]))  # Expected: None
    
    # Test case 5: Two elements
    print("Test 5 (two elements):", get_middle_element([10, 20]))  # Expected: 20
    
    # Test case 6: Large array
    large_arr = list(range(1000000))
    print("Test 6 (large array):", get_middle_element(large_arr))  # Expected: 500000
    
    print("\n--- Complexity Analysis ---")
    print("Time: O(1) - Constant time regardless of array size")
    print("Space: O(1) - Only uses a single variable for the index")
    print("\nKey Insight: Direct array indexing is O(1) because arrays")
    print("store elements contiguously in memory, allowing instant address calculation.")
