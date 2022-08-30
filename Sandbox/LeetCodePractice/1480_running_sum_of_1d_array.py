class Solution:
    def runningSum(self, nums):
        out = []
        out.append(nums[0])
        for index in range(0,len(nums)-1):
            out.append(out[index]+nums[index+1])    
        return(out)
nums = [1,2,3,4]
print(Solution().runningSum(nums))
