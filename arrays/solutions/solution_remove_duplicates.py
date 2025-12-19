"""
Solution: Remove Duplicates from Sorted Array (Challenge 2)

Problem: Remove duplicates from a sorted array in-place.

This demonstrates the two-pointer technique for in-place array modification.
"""


def remove_duplicates(nums):
    """
    Remove duplicates from sorted array in-place using two pointers.
    
    Approach:
    ---------
    Use two pointers:
    - Read pointer (i): scans through entire array
    - Write pointer (write_pos): tracks where to write next unique element
    
    Since array is sorted, duplicates are adjacent. Compare each element
    with the previous one. If different, write it to write_pos.
    
    Args:
        nums: Sorted list of integers (modified in-place)
        
    Returns:
        Integer: new length k (first k elements are unique)
    
    Time Complexity: O(n)
    -----------------
    - Single pass through array: n iterations
    - Each iteration: O(1) operations
    - Total: O(n)
    
    Space Complexity: O(1)
    ------------------
    - Only two pointer variables
    - Modifies array in-place
    - No additional data structures
    
    Examples:
    ---------
    >>> nums = [1, 1, 2]
    >>> k = remove_duplicates(nums)
    >>> print(k, nums[:k])
    2 [1, 2]
    
    >>> nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    >>> k = remove_duplicates(nums)
    >>> print(k, nums[:k])
    5 [0, 1, 2, 3, 4]
    """
    # Edge case: empty array
    if not nums:
        return 0
    
    # Write pointer starts at position 1 (first element always unique)
    write_pos = 1
    
    # Read pointer scans from position 1
    for i in range(1, len(nums)):
        # If current element differs from previous, it's unique
        if nums[i] != nums[i - 1]:
            # Write it to write_pos and advance write pointer
            nums[write_pos] = nums[i]
            write_pos += 1
    
    # write_pos is now the length of unique elements
    return write_pos


def remove_duplicates_alternative(nums):
    """
    Alternative implementation comparing with last written unique element.
    
    Approach:
    ---------
    Compare each element with the last unique element we wrote (at write_pos-1).
    If different, write current element and advance write pointer.
    
    This is slightly different logic but achieves the same result.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not nums:
        return 0
    
    write_pos = 1  # First element always stays
    
    for i in range(1, len(nums)):
        # Compare with last written unique element
        if nums[i] != nums[write_pos - 1]:
            nums[write_pos] = nums[i]
            write_pos += 1
    
    return write_pos


def remove_duplicates_verbose(nums):
    """
    Verbose version with detailed tracking for educational purposes.
    
    Shows exactly what happens at each step.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not nums:
        return 0
    
    print(f"Initial array: {nums}")
    print(f"Length: {len(nums)}\n")
    
    write_pos = 1
    
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            print(f"Step {i}: Found unique element {nums[i]}")
            print(f"  Writing to position {write_pos}")
            nums[write_pos] = nums[i]
            print(f"  Array now: {nums}")
            write_pos += 1
        else:
            print(f"Step {i}: Skip duplicate {nums[i]}")
    
    print(f"\nFinal unique length: {write_pos}")
    print(f"Unique elements: {nums[:write_pos]}")
    
    return write_pos


def remove_duplicates_brute_force(nums):
    """
    INEFFICIENT APPROACH: Using extra space (violates constraints).
    
    Approach:
    ---------
    Create new array with unique elements, then copy back.
    This is NOT allowed by the problem but shows the contrast.
    
    Time Complexity: O(n)
    Space Complexity: O(n) - VIOLATES CONSTRAINT!
    
    Why this is worse:
    - Uses O(n) extra space
    - Slower in practice due to memory allocation
    - Doesn't meet problem requirements
    """
    if not nums:
        return 0
    
    # Create new array with unique elements (EXTRA SPACE!)
    unique = [nums[0]]
    
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            unique.append(nums[i])
    
    # Copy back to original array
    for i in range(len(unique)):
        nums[i] = unique[i]
    
    return len(unique)


# Demonstration and testing
def demonstrate_two_pointer_technique():
    """
    Visual demonstration of the two-pointer technique.
    """
    print("=" * 70)
    print("TWO-POINTER TECHNIQUE VISUALIZATION")
    print("=" * 70)
    print("""
The two-pointer technique uses:
1. READ pointer: Scans through entire array
2. WRITE pointer: Tracks where to place next unique element

Initial state:
    [1, 1, 2, 2, 3]
     ^  ^
     W  R

W = Write pointer (position 1)
R = Read pointer (position 1)

Step 1: nums[1]=1 == nums[0]=1 (duplicate, skip)
    [1, 1, 2, 2, 3]
     ^     ^
     W     R

Step 2: nums[2]=2 != nums[1]=1 (unique! write it)
    [1, 2, 2, 2, 3]
        ^  ^
        W  R

Step 3: nums[3]=2 == nums[2]=2 (duplicate, skip)
    [1, 2, 2, 2, 3]
        ^     ^
        W     R

Step 4: nums[4]=3 != nums[3]=2 (unique! write it)
    [1, 2, 3, 2, 3]
           ^  ^
           W  R

Final: Write pointer at position 3 = length of unique elements
Result: [1, 2, 3] (first 3 elements)
    """)


def compare_approaches(nums):
    """
    Compare different approaches to the problem.
    """
    print(f"\nInput array: {nums}")
    print(f"Length: {len(nums)}\n")
    
    # Test optimal approach
    nums1 = nums.copy()
    k1 = remove_duplicates(nums1)
    print(f"Two-pointer result:")
    print(f"  Length: {k1}")
    print(f"  Unique elements: {nums1[:k1]}")
    print(f"  Time: O(n), Space: O(1) ✓ Optimal")
    
    # Test alternative approach
    nums2 = nums.copy()
    k2 = remove_duplicates_alternative(nums2)
    print(f"\nAlternative result:")
    print(f"  Length: {k2}")
    print(f"  Unique elements: {nums2[:k2]}")
    print(f"  Time: O(n), Space: O(1) ✓ Optimal")
    
    # Test brute force (violates constraints)
    nums3 = nums.copy()
    k3 = remove_duplicates_brute_force(nums3)
    print(f"\nBrute force result (violates O(1) space):")
    print(f"  Length: {k3}")
    print(f"  Unique elements: {nums3[:k3]}")
    print(f"  Time: O(n), Space: O(n) ✗ Not allowed")


# Test cases
if __name__ == "__main__":
    print("=" * 70)
    print("REMOVE DUPLICATES FROM SORTED ARRAY - CHALLENGE 2 SOLUTIONS")
    print("=" * 70)
    
    # Show technique visualization
    demonstrate_two_pointer_technique()
    
    # Test case 1: Basic case
    print("\n" + "=" * 70)
    print("TEST 1: Basic case with duplicates")
    print("=" * 70)
    nums1 = [1, 1, 2]
    k1 = remove_duplicates(nums1)
    print(f"Input: [1, 1, 2]")
    print(f"Output: k = {k1}, nums = {nums1[:k1]}")
    print(f"Expected: k = 2, nums = [1, 2]")
    print(f"Pass: {k1 == 2 and nums1[:2] == [1, 2]}")
    
    # Test case 2: Multiple duplicates
    print("\n" + "=" * 70)
    print("TEST 2: Multiple duplicates")
    print("=" * 70)
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k2 = remove_duplicates(nums2)
    print(f"Input: [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]")
    print(f"Output: k = {k2}, nums = {nums2[:k2]}")
    print(f"Expected: k = 5, nums = [0, 1, 2, 3, 4]")
    print(f"Pass: {k2 == 5 and nums2[:5] == [0, 1, 2, 3, 4]}")
    
    # Test case 3: No duplicates
    print("\n" + "=" * 70)
    print("TEST 3: No duplicates")
    print("=" * 70)
    nums3 = [1, 2, 3, 4, 5]
    k3 = remove_duplicates(nums3)
    print(f"Input: [1, 2, 3, 4, 5]")
    print(f"Output: k = {k3}, nums = {nums3[:k3]}")
    print(f"Expected: k = 5, nums = [1, 2, 3, 4, 5]")
    print(f"Pass: {k3 == 5 and nums3[:5] == [1, 2, 3, 4, 5]}")
    
    # Test case 4: All same elements
    print("\n" + "=" * 70)
    print("TEST 4: All duplicates")
    print("=" * 70)
    nums4 = [1, 1, 1, 1, 1]
    k4 = remove_duplicates(nums4)
    print(f"Input: [1, 1, 1, 1, 1]")
    print(f"Output: k = {k4}, nums = {nums4[:k4]}")
    print(f"Expected: k = 1, nums = [1]")
    print(f"Pass: {k4 == 1 and nums4[:1] == [1]}")
    
    # Test case 5: Empty array
    print("\n" + "=" * 70)
    print("TEST 5: Edge case - empty array")
    print("=" * 70)
    nums5 = []
    k5 = remove_duplicates(nums5)
    print(f"Input: []")
    print(f"Output: k = {k5}")
    print(f"Expected: k = 0")
    print(f"Pass: {k5 == 0}")
    
    # Compare approaches
    print("\n" + "=" * 70)
    print("APPROACH COMPARISON")
    print("=" * 70)
    compare_approaches([1, 1, 2, 2, 2, 3, 4, 4, 5])
    
    # Key insights
    print("\n" + "=" * 70)
    print("KEY INSIGHTS")
    print("=" * 70)
    print("""
1. TWO-POINTER TECHNIQUE FOR IN-PLACE MODIFICATION
   - Read pointer: Scans through array
   - Write pointer: Tracks where to place next element
   - Efficient: O(n) time, O(1) space

2. SORTED ARRAY PROPERTY
   - Duplicates are adjacent
   - Only need to compare consecutive elements
   - Don't need hash set or additional passes

3. IN-PLACE MODIFICATION PATTERN
   - Overwrite array as you scan
   - Write pointer always ≤ read pointer
   - Valid because we're shrinking, not expanding

4. REAL-WORLD APPLICATIONS
   - Database query deduplication (DISTINCT clause)
   - Log file processing (remove duplicate entries)
   - Stream processing (unique values from sorted stream)
   - Data compression (run-length encoding preprocessing)

5. RELATED PROBLEMS
   - Remove Duplicates II: Allow at most 2 duplicates
   - Remove Elements: Remove all instances of a value
   - Move Zeroes: Move all zeros to end
   - All use similar two-pointer pattern!

6. WHY IN-PLACE MATTERS
   - Memory efficiency: No O(n) extra space
   - Cache friendly: Better CPU cache utilization
   - Practical: Many real systems have memory constraints
   - Interview skill: Demonstrates understanding of space complexity
    """)
