# Last updated: 7/22/2025, 12:14:49 AM
class Solution(object):
    def isPalindrome(self, s):
        newstr=""
        for i in s:
            if i.isalnum():
                newstr += i.lower()
        
        left=0
        right=len(newstr)-1
        while(left<right):
            if newstr[left]!=newstr[right]:
                return False
            else:
                left+=1
                right-=1
        return True
        