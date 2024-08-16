# best time to buy and sell stocks
def maxProfit(prices):
    mincost=float('inf')
    max_profit=0
    for i in prices:
        mincost=min(mincost, i)
        max_profit=max(max_profit, i-mincost)
    return max_profit
prices=[7,6,4,3,1]
print(maxProfit(prices))
