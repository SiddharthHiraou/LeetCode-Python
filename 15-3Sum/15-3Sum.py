# Last updated: 7/23/2025, 12:30:16 AM
class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        ans=[]
        for i,a in enumerate(nums):
            if i>0 and a==nums[i-1]:
                continue
            
            l,r=i+1,len(nums)-1
            while(l<r):
                threesum= a+nums[l]+nums[r]
                if threesum==0:
                    ans.append([nums[i],nums[l],nums[r]])

                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    l+=1
                    r-=1

                elif threesum<0:
                    l+=1
                else:
                    r-=1
                
        return ans


        