#!/usr/bin/python3


#Find Numbers with Even Number of Digits
#Given an array nums of integers, return how many of them contain an even number of digits.


from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            if len(str(i))%2 == 0:
                count = count+1
        return count

obj = Solution()
print(obj.findNumbers([12,345,2,6,7896]))
