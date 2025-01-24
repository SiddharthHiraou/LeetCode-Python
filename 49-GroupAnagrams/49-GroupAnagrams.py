class Solution(object):
    def groupAnagrams(self, strs):
        ans=defaultdict(list)
        for ele in strs:
            sorted_word=''.join(sorted(ele))
            ans[sorted_word].append(ele)
        return list(ans.values())
        