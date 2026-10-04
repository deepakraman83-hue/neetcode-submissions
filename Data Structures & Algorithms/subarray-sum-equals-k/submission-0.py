class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count={0:1}
        count,cur_sum=0,0
        for num in nums:
            cur_sum+=num
            if cur_sum-k in prefix_count:
                count+=prefix_count[cur_sum-k]
            prefix_count[cur_sum]=prefix_count.get(cur_sum,0)+1
        return count