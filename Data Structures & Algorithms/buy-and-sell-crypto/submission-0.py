class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        curr_profit = 0
        minValue = prices[0]

        for i in range(1, len(prices)):
            
            profit = prices[i] - minValue

            if curr_profit < profit :
                curr_profit = profit
            if prices[i] < minValue :
                minValue = prices[i]

        return curr_profit