"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums.
More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result.
It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
"""


class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        """
        Idea: Encounter the non-val element - move to the front as we iterate through the array.
        Keep the pointer where to put the non-val element.
        Time - O(n)
        Space - O(1)
        """
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k


mySolution = Solution()

mySolution.removeElement(nums=[0,1,2,2,3,0,4,2], val=2)
