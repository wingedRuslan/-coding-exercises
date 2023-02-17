"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""


class OptimalSolution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Two-pointers technique.
        
        To maximize profit: after encountered valley, find the largest price (peak) following valley.

        Buy when in valley, sell at the highest peak after valley

        Time - O(n)
        Space - O(1)
        """

        maxProfit = 0

        # pointer to track the "valley day" while iterating through array, indicates when to buy
        valley_day = 0

        for curr_day in range(len(prices)):
            
            # update the valley pointer if lower price encountered
            if prices[curr_day] < prices[valley_day]:
                valley_day = curr_day

            # technically we can sell on any day, but check whether results in maxProfit
            maxProfit = max(maxProfit, prices[curr_day] - prices[valley_day])

        return maxProfit


class BruteForceSolutionOptimized:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Straightforward solution: for each price find the highest peak in the future. 
        Keep the maxProfit by comparing the (highest_peak - current price)
		
		Even when optimized, the time complexity remains the same.
		
        Time - O(n**2)
        Space - O(1)
        """
        
        maxProfit = 0

        for i in range(len(prices) - 1):

            # only check valleys
            if prices[i] < prices[i+1]:
                
                # find the largest price following valley - Bottleneck
                high_peak = max(prices[i+1 : ])

                maxProfit = max(maxProfit, high_peak - prices[i])
        
        return maxProfit


class BruteForceSolution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Straightforward solution: for each price find the highest peak in the future. 
        Keep the maxProfit by comparing the (highest_peak - current price)

        Time - O(n**2)
        Space - O(1)
        """
        
        maxProfit = 0

        for i in range(len(prices)):

            high_peak = 0
            for j in range(i+1, len(prices)):
                if prices[j] > high_peak:
                    high_peak = prices[j]
            
            maxProfit = max(maxProfit, high_peak - prices[i])
		
        return maxProfit


