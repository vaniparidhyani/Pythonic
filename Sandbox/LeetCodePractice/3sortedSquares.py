#!/usr/bin/python3

#Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared = list(map(lambda x: x**2, nums))
        return sorted(squared)


print(Solution().sortedSquares([-7,-3,2,3,11]))
