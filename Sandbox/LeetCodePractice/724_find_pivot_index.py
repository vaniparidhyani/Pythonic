#The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

class Solution:
    def pivotIndex(self, nums):
        lsum = 0
        rsum = sum(nums)
        for i in range(len(nums)):
            
            rsum-=nums[i]
            
            if lsum == rsum :
                return(i)
            lsum += nums[i]
            
        return -1
        
print(Solution().pivotIndex([1,7,3,6,5,6]))

