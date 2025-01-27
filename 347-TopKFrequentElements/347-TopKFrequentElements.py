class Solution(object):
    def topKFrequent(self, nums, k):
        freq_dic={}
        for ele in nums:
            if ele in freq_dic:
                freq_dic[ele]+=1
            else:
                freq_dic[ele]=1

        list_sorted=sorted(freq_dic.keys(),key = lambda x: freq_dic[x],reverse=True)

        return list_sorted[:k]
        