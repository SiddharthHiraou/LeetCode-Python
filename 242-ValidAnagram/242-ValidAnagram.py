# Last updated: 7/6/2025, 12:22:03 AM
class Solution(object):
    def isAnagram(self, s, t):
        return Counter(s)==Counter(t)
        