class Solution:
    def bubbleSort(self, nums: List[int]) -> List[int]:
        """
        Bubble Sort algorithm in O(n**2)

        Traverse the array n (=len(nums)) times
        Swap if the element found is greater than the next element
        --> each time the biggest element 'bubbles' at the end of the array

        Time: O(n^2)
        Space: O(1)
        """

        for i in range(len(nums)):
            for j in range(1, len(nums) - i):    # Last i elements are already in place
                if nums[j] < nums[j-1]:
                    nums[j], nums[j-1] = nums[j-1], nums[j]
        
        return nums

