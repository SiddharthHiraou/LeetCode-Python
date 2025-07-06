# Last updated: 7/6/2025, 4:23:44 PM
class Solution(object):
    def topKFrequent(self, nums, k):
        freq_dic={}
        for i in nums:
            if i in freq_dic:
                freq_dic[i]+=1
                continue
            freq_dic[i]=1;
        topk= sorted(freq_dic, key = freq_dic.get, reverse=True)[:k]
        return topk
            
        