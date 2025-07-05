class Solution(object):
    def twoSum(self, nums, target):
        ans={}
        for i,num in enumerate(nums):
            comp=target-num
            if comp in ans:
                return[ans[comp],i]
            ans[num]=i
            
        