class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        boughtFor = 0
        owned = False

        for i in range(len(prices)-1):
            if owned:
                if prices[i] > boughtFor:
                    profit += prices[i] - boughtFor
                    owned = False

            if prices[i+1] > prices[i]:
                boughtFor = prices[i]
                owned = True
        
        if owned:
            profit += prices[len(prices)-1] - boughtFor

        return profit