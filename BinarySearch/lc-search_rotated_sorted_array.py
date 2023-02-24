"""
33. Search in Rotated Sorted Array

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Key: Viz the input array -- after modifying the array, array consists of sorted parts (left and right)
             e.g. [4,5,6,7,0,1,2] -- [4, 5, 6, 7] and [0, 1, 2]. The right array ALWAYS smalled than the left array
        
        Understand the discrete cases (left or right sorted portion), design rules which part to check for target
		
        1. Which part of the array is the mid point: left-sorted or right-sorted
            -- in left sorted portion if nums[mid] >= nums[l], else in the right sorted portion
            -- depending on which part of array the {mid} is --> design rules (2.) to know which part to check next
		
        Time - O(logn)
        Space - O(1)
        """
        
        l = 0
        r = len(nums) - 1

        while l <= r:
            
            mid = (l + r) // 2    # middle value
            
            if target == nums[mid]:
                return mid
            
            # left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:    # search in the right part
                    l = mid + 1    
                else:                                         # nums[l] <= target <= nums[mid] --> search in the left part
                    r = mid - 1
            
            # right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1                               # search in the left part
                else:
                    l = mid + 1                               # nums[mid] < target < nums[r] --> search in the right part


        return -1

