"""
Solution: Trapping Rain Water (Challenge 6)

Problem: Calculate water trapped between elevation bars after rain.

This demonstrates advanced two-pointer technique with state tracking.
"""


def trap(height):
    """
    Calculate trapped water using two pointers.
    
    Approach:
    ---------
    Use two pointers from both ends.
    Track max height seen from left and right.
    Move pointer with smaller max height.
    
    Water at position = min(max_left, max_right) - height[i]
    
    Args:
        height: List of non-negative integers representing elevations
        
    Returns:
        Integer: total water trapped
    
    Time Complexity: O(n) - single pass
    Space Complexity: O(1) - only pointer and max variables
    
    Examples:
    ---------
    >>> trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    6
    >>> trap([4, 2, 0, 3, 2, 5])
    9
    """
    if not height:
        return 0
    
    left = 0
    right = len(height) - 1
    max_left = max_right = 0
    water = 0
    
    while left < right:
        if height[left] < height[right]:
            # Left side determines water level
            if height[left] >= max_left:
                max_left = height[left]
            else:
                water += max_left - height[left]
            left += 1
        else:
            # Right side determines water level
            if height[right] >= max_right:
                max_right = height[right]
            else:
                water += max_right - height[right]
            right -= 1
    
    return water


def trap_with_arrays(height):
    """
    Alternative: Pre-compute max arrays (uses O(n) space).
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if not height:
        return 0
    
    n = len(height)
    max_left = [0] * n
    max_right = [0] * n
    
    # Compute max from left
    max_left[0] = height[0]
    for i in range(1, n):
        max_left[i] = max(max_left[i-1], height[i])
    
    # Compute max from right
    max_right[n-1] = height[n-1]
    for i in range(n-2, -1, -1):
        max_right[i] = max(max_right[i+1], height[i])
    
    # Calculate trapped water
    water = 0
    for i in range(n):
        water += min(max_left[i], max_right[i]) - height[i]
    
    return water


# Test cases
if __name__ == "__main__":
    print("=== Trapping Rain Water - Challenge 6 ===\n")
    
    test_cases = [
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
        ([3, 0, 2, 0, 4], 7)
    ]
    
    for i, (heights, expected) in enumerate(test_cases, 1):
        result = trap(heights)
        print(f"Test {i}:")
        print(f"  Heights: {heights}")
        print(f"  Water:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Pass:    {result == expected}\n")
    
    print("Key Insight: Two pointers with max tracking enables O(1) space!")
