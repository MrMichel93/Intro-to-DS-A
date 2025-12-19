"""
Solution: Find Duplicate Elements (Challenge 5)

Problem: Implement two different solutions - one optimized for space, one for time.

This solution demonstrates space-time tradeoffs in algorithm design.
"""


def find_duplicates_space_optimized(arr):
    """
    Find duplicates by sorting first (space-efficient approach).
    
    Approach:
    ---------
    Sort the array so duplicate values become adjacent. Then scan through
    once to identify duplicates. This minimizes space usage at the cost of
    slower O(n log n) time complexity.
    
    Why it's space-efficient:
    - Only stores the result list (output requirement)
    - No additional hash sets or dictionaries
    - Sorting can be done in-place (though Python's sorted() doesn't)
    
    Args:
        arr: List of integers
        
    Returns:
        List of duplicate values (no duplicates in result)
    
    Time Complexity: O(n log n)
    -----------------
    - Sorting: O(n log n) - dominant operation
    - Single scan: O(n)
    - Total: O(n log n) + O(n) = O(n log n)
    
    Space Complexity: O(1) to O(n)
    ------------------
    - sorted() creates new array: O(n) in Python
    - Result list: O(k) where k = number of duplicates
    - Could be O(1) with in-place sort in other languages
    
    Examples:
    ---------
    >>> find_duplicates_space_optimized([1, 2, 3, 2, 4, 1, 5])
    [1, 2]
    >>> find_duplicates_space_optimized([1, 1, 1, 1])
    [1]
    >>> find_duplicates_space_optimized([1, 2, 3, 4])
    []
    """
    if len(arr) < 2:
        return []
    
    duplicates = []
    
    # Sort the array: O(n log n)
    # After sorting, duplicates will be adjacent
    # [1, 2, 3, 2, 4, 1] → [1, 1, 2, 2, 3, 4]
    sorted_arr = sorted(arr)
    
    # Scan through sorted array: O(n)
    for i in range(1, len(sorted_arr)):
        # Check if current element equals previous
        if sorted_arr[i] == sorted_arr[i-1]:
            # Found a duplicate!
            # Avoid adding same duplicate multiple times
            if not duplicates or duplicates[-1] != sorted_arr[i]:
                duplicates.append(sorted_arr[i])
    
    return duplicates


def find_duplicates_time_optimized(arr):
    """
    Find duplicates using hash set (time-efficient approach).
    
    Approach:
    ---------
    Use a hash set to track seen elements. Hash sets provide O(1) average-case
    lookup, making this approach much faster than sorting. Trade-off is using
    O(n) extra space to store the sets.
    
    Why it's time-efficient:
    - Set membership check: O(1) average case
    - Single pass through array: O(n)
    - No sorting required
    
    Args:
        arr: List of integers
        
    Returns:
        List of duplicate values (no duplicates in result)
    
    Time Complexity: O(n)
    -----------------
    - Single loop: n iterations
    - Set operations (add, check membership): O(1) average
    - Total: O(n)
    
    Space Complexity: O(n)
    ------------------
    - 'seen' set: O(n) - stores up to n unique elements
    - 'duplicates' set: O(k) - stores up to k duplicates
    - Result list conversion: O(k)
    - Total: O(n)
    
    Examples:
    ---------
    >>> find_duplicates_time_optimized([1, 2, 3, 2, 4, 1, 5])
    [1, 2]
    >>> find_duplicates_time_optimized([1, 1, 1, 1])
    [1]
    >>> find_duplicates_time_optimized([1, 2, 3, 4])
    []
    """
    if len(arr) < 2:
        return []
    
    seen = set()           # Track elements we've encountered
    duplicates = set()     # Track duplicates (set prevents duplicate duplicates)
    
    # Single pass through array: O(n)
    for num in arr:
        if num in seen:    # O(1) lookup
            # We've seen this before - it's a duplicate!
            duplicates.add(num)
        else:
            # First time seeing this element
            seen.add(num)  # O(1) insertion
    
    return list(duplicates)


# Alternative Solution 1: Using Counter (Pythonic approach)
def find_duplicates_counter(arr):
    """
    Find duplicates using collections.Counter.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Most Pythonic solution using standard library.
    """
    from collections import Counter
    
    if len(arr) < 2:
        return []
    
    # Count occurrences of each element
    counts = Counter(arr)
    
    # Return elements that appear more than once
    return [num for num, count in counts.items() if count > 1]


# Alternative Solution 2: In-place modification (if allowed to modify input)
def find_duplicates_inplace(arr):
    """
    Find duplicates with minimal extra space using input array modification.
    
    WARNING: This modifies the input array!
    
    Time Complexity: O(n log n) - due to sorting
    Space Complexity: O(1) - sorts in place
    
    Only works if we're allowed to modify the input.
    """
    if len(arr) < 2:
        return []
    
    # Sort the array IN PLACE
    arr.sort()  # O(n log n), but in-place
    
    duplicates = []
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            if not duplicates or duplicates[-1] != arr[i]:
                duplicates.append(arr[i])
    
    return duplicates


# Comparison and Analysis Function
def compare_approaches(arr):
    """
    Compare both approaches with the same input.
    
    Demonstrates the space-time tradeoff in action.
    """
    print(f"Input array: {arr}")
    print(f"Array size: {len(arr)}\n")
    
    # Space-optimized approach
    result1 = find_duplicates_space_optimized(arr)
    print("Space-Optimized (Sorting):")
    print(f"  Result: {result1}")
    print(f"  Time: O(n log n)")
    print(f"  Space: O(1) for algorithm (O(n) in Python for sorted())")
    print()
    
    # Time-optimized approach
    result2 = find_duplicates_time_optimized(arr)
    print("Time-Optimized (Hash Set):")
    print(f"  Result: {sorted(result2)}")  # Sort for comparison
    print(f"  Time: O(n)")
    print(f"  Space: O(n) for hash set")
    print()
    
    return result1, result2


# Performance comparison with larger data
def performance_analysis():
    """
    Analyze performance characteristics with different input sizes.
    """
    print("=== Performance Analysis ===\n")
    
    test_sizes = [10, 100, 1000, 10000]
    
    for size in test_sizes:
        # Create array with some duplicates
        arr = list(range(size // 2)) * 2  # Each number appears twice
        
        print(f"Array size: {size}")
        print(f"  Space-Optimized: ~{size * (size.bit_length())} operations (n log n)")
        print(f"  Time-Optimized:  ~{size} operations (n)")
        print(f"  Speedup: {size.bit_length()}x faster\n")


# Test cases
if __name__ == "__main__":
    print("=== Finding Duplicates: Space vs Time Trade-off ===\n")
    
    # Test case 1: Regular array with duplicates
    test1 = [1, 2, 3, 2, 4, 1, 5]
    print("Test 1: Regular array")
    compare_approaches(test1)
    print("-" * 60)
    
    # Test case 2: All duplicates
    test2 = [1, 1, 1, 1]
    print("\nTest 2: All same elements")
    compare_approaches(test2)
    print("-" * 60)
    
    # Test case 3: No duplicates
    test3 = [1, 2, 3, 4, 5]
    print("\nTest 3: No duplicates")
    compare_approaches(test3)
    print("-" * 60)
    
    # Test case 4: Multiple duplicates
    test4 = [5, 3, 5, 2, 3, 1, 5, 2]
    print("\nTest 4: Multiple different duplicates")
    compare_approaches(test4)
    print("-" * 60)
    
    # Performance analysis
    print("\n")
    performance_analysis()
    
    # Key insights
    print("=== Key Insights ===")
    print("\n1. SPACE-TIME TRADEOFF:")
    print("   - Can't always optimize both simultaneously")
    print("   - Must choose based on constraints")
    print("\n2. WHEN TO USE SPACE-OPTIMIZED:")
    print("   - Limited memory (embedded systems, mobile)")
    print("   - Small datasets where O(n log n) is acceptable")
    print("   - Cannot allocate O(n) extra space")
    print("\n3. WHEN TO USE TIME-OPTIMIZED:")
    print("   - Large datasets where speed matters")
    print("   - Memory is available")
    print("   - Need real-time or low-latency response")
    print("\n4. REAL-WORLD EXAMPLE:")
    print("   - Mobile app (limited memory) → Use sorting")
    print("   - Backend server (abundant memory) → Use hash set")
    print("   - Need both? → Use hybrid approaches or caching")
