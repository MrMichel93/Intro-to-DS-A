"""
Solution: Product of Array Except Self (Challenge 3)

Problem: Calculate the product of all elements except the current one without division.

This demonstrates prefix/suffix product techniques for complex calculations.
"""


def product_except_self(nums):
    """
    Calculate product of all elements except self using prefix/suffix products.
    
    Approach:
    ---------
    For position i, result[i] = (product of all left) × (product of all right)
    
    Use two passes:
    1. Left to right: calculate prefix products
    2. Right to left: multiply by suffix products
    
    Args:
        nums: List of integers
        
    Returns:
        List where output[i] = product of all nums except nums[i]
    
    Time Complexity: O(n) - two passes
    Space Complexity: O(1) - output array doesn't count
    
    Examples:
    ---------
    >>> product_except_self([1, 2, 3, 4])
    [24, 12, 8, 6]
    >>> product_except_self([-1, 1, 0, -3, 3])
    [0, 0, 9, 0, 0]
    """
    n = len(nums)
    result = [1] * n
    
    # Pass 1: Calculate prefix products (left to right)
    # result[i] = product of all elements to the left of i
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]
    
    # Pass 2: Multiply by suffix products (right to left)
    # result[i] *= product of all elements to the right of i
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
    
    return result


def product_except_self_with_division(nums):
    """
    SIMPLER BUT NOT ALLOWED: Using division.
    
    Calculate total product, then divide by each element.
    Problem specifically prohibits division!
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    n = len(nums)
    result = [0] * n
    
    # Calculate total product
    total_product = 1
    zero_count = 0
    zero_index = -1
    
    for i, num in enumerate(nums):
        if num == 0:
            zero_count += 1
            zero_index = i
        else:
            total_product *= num
    
    # Handle zero cases
    if zero_count > 1:
        return result  # All zeros
    elif zero_count == 1:
        result[zero_index] = total_product
        return result
    
    # No zeros: divide for each position
    for i in range(n):
        result[i] = total_product // nums[i]
    
    return result


# Test cases
if __name__ == "__main__":
    print("=== Product of Array Except Self - Challenge 3 ===\n")
    
    test_cases = [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
        ([2, 3, 4, 5], [60, 40, 30, 24])
    ]
    
    for i, (input_arr, expected) in enumerate(test_cases, 1):
        result = product_except_self(input_arr)
        print(f"Test {i}:")
        print(f"  Input:    {input_arr}")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Pass:     {result == expected}\n")
    
    print("Key Insight: Prefix/suffix products enable O(n) solution without division!")
