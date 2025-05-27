# Last updated: 5/27/2025, 9:30:32 PM
class Solution(object):
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
    
        while left <= right:
            mid = left + (right - left) // 2 
        
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
    
        return -1 
        