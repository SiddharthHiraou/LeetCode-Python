# Last updated: 7/6/2025, 12:46:12 AM
class Solution(object):
    def groupAnagrams(self, strs):
        ans=defaultdict(list)
        for i in strs:
            key=''.join(sorted(i))
            ans[key].append(i)
        return list(ans.values())

        