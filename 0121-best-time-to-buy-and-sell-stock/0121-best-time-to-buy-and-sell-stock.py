class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        p1=0
        p2=1
        max_profit = 0
        
        while p2<len(prices):
            if prices[p1]<prices[p2]:
                profit=prices[p2]-prices[p1]
                max_profit = max(max_profit,profit)
            else:
                p1=p2
            p2+=1
        return max_profit
        