
#525 contigous array-Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
#Example 1:

#Input: nums = [0,1]
#Output: 2
#Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
#Example 2:

#Input: nums = [0,1,0]
#Output: 2
#Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        cur_sum=0
        sum_indices={0:1}
        max_length=0
        for i in range(len(nums)):
            if nums[i]==1:
                cur_sum+=1
            else:
                cur_sum-=1
            if cur_sum in sum_indices:
                max_length=max(max_length,i-sum_indices[cur_sum])
            else:
                sum_indices[cur_sum]=i
        return max_length
