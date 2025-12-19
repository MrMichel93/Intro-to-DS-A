'''Solution: Split Array Largest Sum (Challenge 6)'''
def split_array(nums, k):
    def can_split(max_sum):
        count, current = 1, 0
        for num in nums:
            if current + num > max_sum:
                count += 1
                current = num
                if count > k:
                    return False
            else:
                current += num
        return True
    
    left, right = max(nums), sum(nums)
    while left < right:
        mid = left + (right - left) // 2
        if can_split(mid):
            right = mid
        else:
            left = mid + 1
    return left
