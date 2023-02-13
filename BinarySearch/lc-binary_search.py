"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

All the integers in nums are unique.
nums is sorted in ascending order.
"""


class RecursiveSolution:
    def search(self, nums: List[int], target: int) -> int:
                
        def _recursive_search(nums, start, end, target):
            
            # Base case 
            if start > end:
                return -1
            
            mid = (start + end) // 2

            if nums[mid] > target:
                return _recursive_search(nums, start, mid - 1, target)
            elif nums[mid] < target:
                return _recursive_search(nums, mid + 1, end, target)
            else:
                return mid

        ans = _recursive_search(nums, 0, len(nums)-1, target)

        return ans


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Time - O(log n)
        
        {nums} is divided into half each time. 
        In the worst-case scenario, we need to cut nums until the range has no element, 
        	and it takes logarithmic time to reach this break condition.
        
        Space - O(1)
        """
        
        # define search space
        start = 0
        end = len(nums) - 1

        while start <= end:
            
            mid = (start + end) // 2

            if nums[mid] > target:    # look in the left part for target 
                end = mid - 1
            elif nums[mid] < target:  # look in the right part for target
                start = mid + 1
            else:                     # case if found
                return mid
		
        return -1

