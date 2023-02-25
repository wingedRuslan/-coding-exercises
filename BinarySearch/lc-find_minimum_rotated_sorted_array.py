"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Array contains two portitions that are sorted: left and right, elements in left > elements in right.

        Desing rules for BinarySearch to always loop for minValue in the smallest subspace.
        
        Time - O(log n)
        Space - O(1)
        """

        minValue = 5001    # -5000 <= nums[i] <= 5000
        
        l, r = 0, len(nums) - 1

        while l <= r:
            
            # Optimization - if current search space is already sorted --> return element at position l
            if nums[l] < nums[r]:
                minValue = min(minValue, nums[l])
                break

            mid = (l + r ) // 2

            # Lookup the min Element in the smallest subspace
            minValue = min(minValue, nums[mid])

            # Left-sorted portion
            if nums[l] <= nums[mid]:
                minValue = min(minValue, nums[l])
                l = mid + 1
            # Right-sorted portition
            else:
                if nums[mid] <= nums[r]:
                    minValue = min(minValue, nums[mid])
                    r = mid - 1
        
        return minValue

