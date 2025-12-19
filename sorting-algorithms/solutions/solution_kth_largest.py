'''Solution: Kth Largest Element (Challenge 3)'''
import random

def find_kth_largest(nums, k):
    def quickselect(left, right):
        pivot = random.randint(left, right)
        nums[pivot], nums[right] = nums[right], nums[pivot]
        store_index = left
        for i in range(left, right):
            if nums[i] < nums[right]:
                nums[i], nums[store_index] = nums[store_index], nums[i]
                store_index += 1
        nums[store_index], nums[right] = nums[right], nums[store_index]
        if store_index == len(nums) - k:
            return nums[store_index]
        elif store_index < len(nums) - k:
            return quickselect(store_index + 1, right)
        else:
            return quickselect(left, store_index - 1)
    return quickselect(0, len(nums) - 1)
