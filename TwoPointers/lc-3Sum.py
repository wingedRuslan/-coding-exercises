"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""


class TwoPointerSolution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Idea: 1) Sort the array
              2) Two-pointer technique apply to search for the 2 elements which sum up with current element to 0 
              	For each element, 
                    find two other elements that sum to 0 - ( same as Two Sum 2 problem)
                Pay attention to 'Notice that the solution set must not contain duplicate triplets'
        
        Time - O(nlogn) + O(n**2) = O(n**2)
        Space - O(1) or O(n) - sorting might use space depanding on the algorithm
        """

        # Array to return
        res = []
        
        # O(n logn)
        nums.sort()

        ind = 0
        while ind < len(nums) - 2:

            # Use Two Pointers to find out if there exist sum(2 elements) + nums[ind] == 0
            l = ind + 1
            r = len(nums) - 1

            target = - (nums[ind])

            while l < r:

                curSum = nums[l] + nums[r]
                
                if curSum < target:    # if too small sum -- make the sum bigger
                    l += 1
                elif curSum > target:  # if too large sum -- make the sum smaller
                    r -= 1
                else:
                    res.append([nums[ind], nums[l], nums[r]])      # Found the triplet!
                    l += 1                                         # Update either l or r
                    while (nums[l] == nums[l - 1]) and (l < r):    # Make sure to skip repetitions
                        l += 1
            
            # Skip repetitions of the same element because "solution set must not contain duplicate triplets"
            while ind < len(nums) and nums[ind] == -target:
                ind += 1

        return res

