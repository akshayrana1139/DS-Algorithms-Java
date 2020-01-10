# Runtime: 64 ms, faster than 57.57% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 13.8 MB, less than 98.85% of Python3 online submissions for Best Time to Buy and Sell Stock.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = float("inf")
        profit = 0 
        for i in range(len(prices)):
            if prices[i]<minimum:
                minimum = prices[i]
            elif ((prices[i]-minimum) > profit):
                profit = prices[i] - minimum
        return profit
                
            
                
            