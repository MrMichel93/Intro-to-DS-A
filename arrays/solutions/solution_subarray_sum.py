"""
Solution: Find All Subarrays with Given Sum (Challenge 5)

Problem: Find all contiguous subarrays that sum to target.

This demonstrates prefix sum with hash map technique.
"""


def subarray_sum(nums, target):
    """
    Find all subarrays that sum to target using prefix sums.
    
    Approach:
    ---------
    Use prefix sum: if prefix[j] - prefix[i] = target,
    then subarray from i+1 to j sums to target.
    
    Store each prefix sum with all indices where it occurs.
    
    Args:
        nums: List of integers
        target: Target sum to find
        
    Returns:
        List of [start, end] pairs for subarrays that sum to target
    
    Time Complexity: O(n) - single pass
    Space Complexity: O(n) - hash map storage
    
    Examples:
    ---------
    >>> subarray_sum([1, 2, 3, 4, 5], 9)
    [[1, 3], [3, 4]]
    >>> subarray_sum([1, 1, 1], 2)
    [[0, 1], [1, 2]]
    """
    result = []
    prefix_sum = 0
    prefix_map = {0: [-1]}  # prefix_sum: [list of indices]
    
    for i in range(len(nums)):
        prefix_sum += nums[i]
        
        # Look for (prefix_sum - target) in map
        complement = prefix_sum - target
        if complement in prefix_map:
            # Found subarrays ending at i
            for start_idx in prefix_map[complement]:
                result.append([start_idx + 1, i])
        
        # Store current prefix sum
        if prefix_sum not in prefix_map:
            prefix_map[prefix_sum] = []
        prefix_map[prefix_sum].append(i)
    
    return result


# Test cases
if __name__ == "__main__":
    print("=== Find All Subarrays with Given Sum - Challenge 5 ===\n")
    
    test_cases = [
        ([1, 2, 3, 4, 5], 9, [[1, 3], [3, 4]]),
        ([1, 1, 1], 2, [[0, 1], [1, 2]]),
    ]
    
    for i, (nums, target, expected) in enumerate(test_cases, 1):
        result = subarray_sum(nums, target)
        print(f"Test {i}:")
        print(f"  Array:    {nums}")
        print(f"  Target:   {target}")
        print(f"  Result:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Pass:     {result == expected}\n")
    
    print("Key Insight: Prefix sums convert range queries to O(1) lookups!")
