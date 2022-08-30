class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        out = []
        out.append(nums[0])
        for index in range(0,len(nums)-1):
            out.append(out[index]+nums[index+1])    
        return(out)
print(Solution.runningSum())
