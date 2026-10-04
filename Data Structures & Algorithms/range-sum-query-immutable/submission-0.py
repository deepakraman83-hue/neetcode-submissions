class NumArray:
  def __init__(self, nums: list[int]):
     self.prefix_nums=[0]*len(nums)
     self.prefix_nums[0]=nums[0]
     for n in range(1,len(nums)):
        self.prefix_nums[n]=self.prefix_nums[n-1]+nums[n]
  def sumRange(self, left: int, right: int):
    if left == 0:
      result=self.prefix_nums[right]
    else:
      result= self.prefix_nums[right]-self.prefix_nums[left-1]
    return result