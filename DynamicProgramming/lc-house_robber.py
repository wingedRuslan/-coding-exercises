"""
House Robber

You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
"""


class TopDownDPSolution:
    def rob(self, nums: List[int]) -> int:
    	"""
    	More intuitive solution if start robing from the end of the nums.
    	
    	Although the *rule* is very simillar: 	
	    
	    - maxProfit(current house) = max(current house + maxProfit at two location after OR maxProfit at one location after)
    	
    	Time: O(n)
    	Space: O(n) - potentially optimized to O(1) by tracking just two variables
    	"""

        # Base case
        if len(nums) == 1: return nums[0]
        
        # Keep track of MaxProfits at each location
        # end --> start 
        maxProfits = [0] * len(nums)

        maxProfits[-1] = nums[-1]   # last loc profit - just last house
        maxProfits[-2] = max(nums[-1], nums[-2]) # last 2 locs profit - max(in either two last houses)

        # start from the 3rd last house at the end, move --> start
        for loc in range(len(nums) - 3, -1, -1):
            # at each loc either skip house, or rob it
            maxProfits[loc] = max(maxProfits[loc+1], maxProfits[loc+2] + nums[loc])
        
        return maxProfits[0]


class BottomUpDPSolution:
    def rob(self, nums: List[int]) -> int:
        """
        Define a *rule* to whether or not to rob the house at current location or skip it.
        
        Get the max money from the list:
        - rob 1st house @ 0, find the max of the remaining houses [2:n]
        - skip 1st @ 0, find the max of the ramaining houses [1:n]

        rob = max( arr[0] + rob[2:n], rob[1:n] )
            --> break down into subproblems
            --> each rob (=subproblem) can be broken into smaller subproblems
        
        Example:
        [1, 2, 3, 1]

        1 |          - max we get after only 1 house - 1
        1, 2 |       - what is max we rob up until this point? - 2 = max(2, 1)
        1, 2, 3 |    - what is max we rob up until this point? - 4 = max(rob(3,1), rob(2))
        1, 2, 3, 1 | - if decide rob house 1, what was max 2 locations ago (=2) or 
                       do not rob house 1 (what was max 1 location ago = 4)?
        
        RULE!!: rob(current house?) = max( sum 2 locations ago + curr sum ; sum 1 location ago)

        -----
        ps. not just naively odd/even locations, e.g. cases like
            - [2, 1, 1, 2]
            - [1, 3, 1, 3, 100]
        
        Time: O(n)
        Space: O(n), but optimized to O(1) since look at last 2 results at each loc
        """

        # Base case
        if len(nums) == 1: return nums[0]

        # Keep track of MaxProfits at each location
        maxProfits = [0] * len(nums)

        maxProfits[0] = nums[0]               # 1 house - rob it
        maxProfits[1] = max(nums[0], nums[1]) # 2 houses - rob max(nums[0], nums[1])

        for loc in range(2, len(nums)):
            maxProfits[loc] = max(maxProfits[loc - 2] + nums[loc], maxProfits[loc - 1])

        return maxProfits[-1]


