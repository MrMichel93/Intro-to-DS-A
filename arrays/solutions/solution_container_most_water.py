"""
Solution: Container With Most Water (Challenge 4)

Problem: Find two lines that form a container with maximum water capacity.

This demonstrates greedy two-pointer optimization.
"""


def max_area(height):
    """
    Find maximum water container area using two pointers.
    
    Approach:
    ---------
    Start with widest container (pointers at both ends).
    Move the pointer pointing to shorter line inward.
    
    Why? Moving taller line cannot increase area since:
    - Width decreases
    - Height is limited by shorter line
    
    Args:
        height: List of non-negative integers representing line heights
        
    Returns:
        Integer: maximum water area
    
    Time Complexity: O(n) - single pass with two pointers
    Space Complexity: O(1) - only pointer variables
    
    Examples:
    ---------
    >>> max_area([1, 8, 6, 2, 5, 4, 8, 3, 7])
    49
    >>> max_area([1, 1])
    1
    """
    left = 0
    right = len(height) - 1
    max_water = 0
    
    while left < right:
        # Calculate current area
        width = right - left
        current_height = min(height[left], height[right])
        current_area = width * current_height
        
        # Update maximum
        max_water = max(max_water, current_area)
        
        # Move pointer pointing to shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_water


# Test cases
if __name__ == "__main__":
    print("=== Container With Most Water - Challenge 4 ===\n")
    
    test_cases = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([4, 3, 2, 1, 4], 16)
    ]
    
    for i, (heights, expected) in enumerate(test_cases, 1):
        result = max_area(heights)
        print(f"Test {i}:")
        print(f"  Heights:  {heights}")
        print(f"  Max Area: {result}")
        print(f"  Expected: {expected}")
        print(f"  Pass:     {result == expected}\n")
    
    print("Key Insight: Greedy two-pointer - always move the shorter line!")
