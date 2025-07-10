# Last updated: 7/10/2025, 10:16:49 PM
class Solution(object):
    def longestConsecutive(self, nums):
        longest=0
        num_set=set(nums)
        for i in num_set:
            if i-1 not in num_set:
                current= i
                length=1
                while current+1 in num_set:
                    current+=1
                    length+=1
                longest=max(longest,length)
        return longest
        
        