        n = len(nums)
        ans=[1]*n
        left = 1
        for i in range(n):
            ans[i]=left
            left*=nums[i]
        right=1
        for i in reversed(range(n)):
            ans[i]*=right
            right*=nums[i]
        return ans