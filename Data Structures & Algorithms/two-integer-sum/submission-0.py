class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference =0
        check_hash={}
        for i,index in enumerate(nums):
            difference=target-index
            if difference in check_hash:
                return [check_hash[difference],i]

            check_hash[index]=i
        return []


        
        