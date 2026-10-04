class Solution:
  def pivotIndex(self,nums):
    total_sum=sum(nums)
    left_sum=0
    for n in range(len(nums)):
      if left_sum==total_sum-nums[n]-left_sum:
        return n
      left_sum+=nums[n]
    return -1   