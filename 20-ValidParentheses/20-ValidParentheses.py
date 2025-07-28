# Last updated: 7/29/2025, 1:55:06 AM
class Solution(object):
    def isValid(self, s):
        mapdic={")":"(","]":"[","}":"{"}
        stack=[]
        for char in s:
            if char in mapdic:
                top_ele=stack.pop() if stack else '#'
                if mapdic[char]!= top_ele:
                    return False
            else:
                stack.append(char)
        return not stack

        