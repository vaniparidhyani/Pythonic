#!/usr/bin/python3

from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        hi = []
        count = 0
        for i in nums:
            if i == 1:
                count = count + 1
                hi.append(count)
            else:
                count = 0
                hi.append(count)
        return max(hi)

obj = Solution()
print(obj.findMaxConsecutiveOnes([1,1,0,1,1,1]))
