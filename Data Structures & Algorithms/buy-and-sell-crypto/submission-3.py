class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit=0

        if len(prices) <2:
            return 0
        if len(prices) ==2:
            return max(max_profit,prices[1]-prices[0])
        for i in range(0,len(prices)-1):

            j=i+1

            while(j<=len(prices)-1):

                profit=prices[j] - prices[i]
                max_profit=max(max_profit, profit)

                j+=1

        return max_profit
            
        