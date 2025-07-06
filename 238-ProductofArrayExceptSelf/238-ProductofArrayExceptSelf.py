# Last updated: 7/7/2025, 12:58:15 AM
class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        ans=[1]*n
        left = 1
        for i in range(n):
            ans[i]=left
            left*=nums[i]
        right=1
        for i in reversed(range(n)):
            ans[i]*=right
            right*=nums[i]
        return ans