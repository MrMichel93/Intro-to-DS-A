'''Solution: First and Last Position (Challenge 2)'''
def search_range(nums, target):
    def find_boundary(is_first):
        left, right = 0, len(nums) - 1
        boundary = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                boundary = mid
                if is_first:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return boundary
    return [find_boundary(True), find_boundary(False)]
