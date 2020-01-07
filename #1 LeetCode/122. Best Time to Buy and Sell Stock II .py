from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i = 1
        minimum = maximum = prices[0]
        buy = False
        while(i<len(prices)):
            if buy:
                if prices[i]>maximum:
                    maximum = prices[i]
                    if i==len(prices)-1:
                            buy = False # Sold
                            profit += maximum-minimum
                else:
                    buy = False # Sold
                    profit += maximum-minimum
                    minimum = prices[i]
                
            else:
                if prices[i]<minimum:
                    minimum = prices[i]
                    maximum = minimum
                else:
                    buy = True 
                    if prices[i]>maximum:
                        maximum = prices[i]
                        

                    
            i+=1
        return profit


if __name__ == "__main__":
    # print(Solution().maxProfit([1,2,3,4,5]))
    # print(Solution().maxProfit([7,1,5,3,6,4]))
    print(Solution().maxProfit([2,1,2,0,1]))