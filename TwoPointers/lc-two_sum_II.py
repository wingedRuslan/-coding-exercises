"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
"""


class TwoPointerSolution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Set two pointers (l, r) at the start and at the end.
        
        Rule how to move pointers:
            Array sorted in non-decreasing order:
            - if sum(elements at l and r) > target -- move r to the left (decrease sum)
            - if sum(elements at l and r) < target -- move l to the right (increase sum)
        Time - O(n)
        Space - O(1)
        """
        
        l, r = 0, len(numbers) - 1

        while l < r:

            curSum = numbers[l] + numbers[r]
            
            if curSum > target:    # descrease sum
                r -= 1
            elif curSum < target:    # increase sum
                l += 1
            else:
                return [l+1, r+1]

        return -1


class BinarySearchSolution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        BinarySearch Solution
        Idea: for each num in {numbers}, binary_search whether (target - num) exist

        Caveat: e.g. [1,2,3,4,4,9,56,90], t = 8 - when repetitions exist. 
        Max only 2 repetitions due to the constraint - 'The tests are generated such that there is exactly one solution.'
        Still binary search finds the 1st occurence of 4. 
        Solution: add postprocessing - 
        -   if repetition found, just increase the  complement_ind + 1 (point to the same element but next index)
        
        Time - O(n * log(n))
        Space - O(1)
        """

        def _binary_search(nums, target):
            start, end = 0, len(nums) - 1
			
            while start <= end:

                mid = (start + end) // 2

                if nums[mid] == target: return mid

                if nums[mid] < target:
                    start = mid + 1
                elif nums[mid] > target:
                    end = mid - 1

            return -1


        for ind in range(len(numbers)):
            
            # Binary search for (target - numbers[ind])
            complement_ind = _binary_search(numbers, target - numbers[ind])

            # Found the complement number - but case when repetitions exist 
            if complement_ind >= 0 and (ind != complement_ind):
                return [ind + 1, complement_ind + 1]
            elif complement_ind >= 0 and (ind == complement_ind):
                return [ind + 1, complement_ind + 2]

        return -1


