#!/usr/bin/python3

#Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#The number of elements initialized in nums1 and nums2 are m and n respectively. You may assume that nums1 has a size equal to m + n such that it has enough space to hold additional elements from nums2.

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #
        del nums1[m:]
        del nums2[n:]
        nums1.extend(nums2)
        nums1.sort()
        return nums1

obj = Solution()
print(obj.merge([1,2,3,0,0,0],3,[2,5,6],3))
