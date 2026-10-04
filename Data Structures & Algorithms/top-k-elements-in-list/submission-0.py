from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        dd={}
        for n in nums:
          dd[n]=dd.get(n,0)+1
          #print(dd)
        sorted_list=sorted(dd,key=dd.get,reverse=True)
        return sorted_list[:k]



ss=Solution()
print(ss.topKFrequent([1,2,2,3,3,3],2))