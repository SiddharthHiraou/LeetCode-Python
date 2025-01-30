class Solution(object):
    def productExceptSelf(self, nums):
        n=len(nums)
        ans=[1]*n
        prefix=1
        for i in range(n):
            ans[i]=prefix
            prefix*=nums[i]
        suffix=1
        for i in reversed(range(n)):
            ans[i]*=suffix
            suffix*=nums[i]
        return ans
        