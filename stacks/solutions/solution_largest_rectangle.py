"""
Solution: Largest Rectangle in Histogram (Challenge 5)

Problem: Find maximum rectangular area in histogram.
Advanced monotonic stack application.
"""


def largest_rectangle_area(heights):
    """
    Find largest rectangle using monotonic increasing stack.
    
    Approach: Maintain stack of indices with increasing heights.
    When shorter bar found, pop taller bars and calculate their max area.
    
    Time Complexity: O(n) - each bar pushed/popped once
    Space Complexity: O(n) - stack size
    
    Examples:
    >>> largest_rectangle_area([2, 1, 5, 6, 2, 3])
    10
    """
    stack = []
    max_area = 0
    heights = heights + [0]  # Sentinel to process remaining bars
    
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    
    return max_area


if __name__ == "__main__":
    tests = [
        ([2, 1, 5, 6, 2, 3], 10),
        ([2, 4], 4),
        ([1, 1, 1, 1, 1], 5)
    ]
    for heights, expected in tests:
        result = largest_rectangle_area(heights)
        print(f"{heights}: {result} (expected {expected})")
