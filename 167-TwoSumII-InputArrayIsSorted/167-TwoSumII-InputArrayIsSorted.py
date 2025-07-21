# Last updated: 7/22/2025, 12:55:48 AM
class Solution(object):
    def twoSum(self, numbers, target):
        left=0
        right=len(numbers)-1
 
        while(left<right):
            cur_sum= numbers[left]+numbers[right]
            if cur_sum==target:
                return[left+1,right+1]
            elif cur_sum<target:
                left+=1
            else:
                right-=1

        