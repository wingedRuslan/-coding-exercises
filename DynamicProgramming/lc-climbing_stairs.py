"""
Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
 
Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps


Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

##########
# DP Solution
##########
class DPSolution:
    def climbStairs(self, n: int) -> int:
        """
        Bottom-Up Dynamic Programming Approach.
            -> Start at the base case and work the way up.
        
        To climb to step i = (to climb to step i-1) + (to climb to step i-2)
        Keep track of the num. ways to climb to step i in array.

        Time: O(n)
        Space: O(n), but optimize by having only 2 different variables --> O(1) 
        """

        # Base Case
        if n < 2:
            return n

        
        numWaysReachNStairs = [0] * n

        # Base Cases
        numWaysReachNStairs[0] = 1
        numWaysReachNStairs[1] = 2

        for i in range(2, n):
            numWaysReachNStairs[i] = numWaysReachNStairs[i-1] + numWaysReachNStairs[i-2]
        
        return numWaysReachNStairs[-1]


class RecursiveSolution:

    # Keep track of the number of ways to reach N stairs
    # Init with base cases 
    numWaysReachN = {0:0, 1:1, 2:2}

    def climbStairs(self, n: int) -> int:
        """
        Top-down approach:
        -> num ways to get to step n = num ways to get to (n-1) + num ways to get to (n-2) 
        -> recursion w/ memoization

        Time: O(n)
        Space: O(n)
        """
        
        if n in self.numWaysReachN:
            return self.numWaysReachN[n]
        
        n_ways = self.climbStairs(n-1) + self.climbStairs(n-2)

        self.numWaysReachN[n] = n_ways

        return n_ways


