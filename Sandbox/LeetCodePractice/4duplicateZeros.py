#!/usr/bin/python3

#Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.
#Note that elements beyond the length of the original array are not written.
#Do the above modifications to the input array in place, do not return anything from your function.

from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        length = len(arr)
        i = 0
        while i < length:
            if arr[i] == 0 and len(arr) <= length:

                arr.insert(i+1,0)
                arr.pop()

                i = i+2
            else:

                i = i+1
        print(arr)


obj = Solution()
obj.duplicateZeros([1,0,2,3,0,4,5,0])
