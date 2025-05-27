# Last updated: 5/27/2025, 9:30:43 PM
class Solution(object):
    def threeSum(self, nums):
        nums.sort() 
        res = set()
        for i in range(len(nums)):
            target = -nums[i] 
            seen = set()
        
            for j in range(i + 1, len(nums)):
                complement = target - nums[j]
            
                if complement in seen:
                    res.add((nums[i], complement, nums[j]))
                else:
                    seen.add(nums[j])
    
        return [list(triplet) for triplet in res]
        