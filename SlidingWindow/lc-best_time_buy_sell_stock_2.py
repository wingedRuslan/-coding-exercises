class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Visualize the dynamics and spot the patters when to buy/sell. 

        Profit = add every increase of the stock price (every time the array in increasing order), meaning prices[i+1] > prices[i]
        
        Time - O(n)
        Space - O(1)
        """

        profit = 0

        day = 0
        while day < len(prices) - 1: 
            if prices[day] < prices[day + 1]:    # identify increasing price
                profit += (prices[day + 1] - prices[day])
            day += 1

        return profit

