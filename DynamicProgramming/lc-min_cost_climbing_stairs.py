"""
Min Cost Climbing Stairs

You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

Example 1:
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

Example 2:
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
"""


class TopDownDPSolution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Top-Down DP Solution
        
        Start from the top of the floor, keep track of min cost at each step.
        --> check the lowest cost at index 0 or 1
		
		Keep track of the min cost at step i in the original array.
		
        Time: O(n)
        Space: O(1)
        """

        # Top of the floor = the position after len(cost)
        # To maka math work out - add cost of 0
        cost.append(0)
        
        # start @ the index with the 2 steps after it 
        for step in range(len(cost)-3, -1, -1):
            cost[step] = min(cost[step + 1], cost[step + 2]) + cost[step]

        # You can either start from the step with index 0, or the step with index 1
        return min(cost[0], cost[1])


class BottomUpDPSolution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Bottom-Up solution - start with base cases and work the way up.
        
        Use helper array to maintain the min cost it takes to reach index i.

        "Once you pay the cost, you can either climb one or two steps."
        To calculate the min cost at position i (~ Min cost at i):
            - pay the cost at i e.g. cost[i]
            - min( cost at i-1 ; cost at i-2 )

        Top of the floor = the position after len(cost)
        
        Time: O(n)
        Space: O(n) - might optimize by using original input array or just two variables
        """

        # min cost to reach position i
        minCostStep = [0] * len(cost)

        # base cases
        # "You can either start from the step i=0, or the step i=1"
        minCostStep[0] = cost[0]
        minCostStep[1] = cost[1]    # more accurate - min(cost[1] + 0, cost[1] + cost[0])

        for step in range(2, len(cost)):
            minCostStep[step] = min(minCostStep[step-1], minCostStep[step-2]) + cost[step]

        # reach the top either by having one step or two steps
        return min(minCostStep[-1], minCostStep[-2])


