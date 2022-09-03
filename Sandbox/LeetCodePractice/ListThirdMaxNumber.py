#Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max1 = max(nums)
        nums = [x for x in nums if x!=max1]            
        if len(nums):
            max2 = max(nums)
            nums = [x for x in nums if x!=max2]
            if len(nums):
                max3 = max(nums)
                return(max3)
        return(max1)
