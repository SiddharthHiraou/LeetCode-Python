                    while l<r and nums[r]==nums[r-1]:
                        l+=1
                    while l<r and nums[l]==nums[l+1]:
                    ans.append([nums[i],nums[l],nums[r]])
                if threesum==0:
                threesum= a+nums[l]+nums[r]
            while(l<r):
            l,r=i+1,len(nums)-1
            
                continue
            if i>0 and a==nums[i-1]: