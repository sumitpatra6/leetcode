class Solution:
    def maxProfit(self, prices):
        profit = 0
        curr_share = prices[0]
        min_till_now = prices[0]
        max_till_now = prices[0]
        for i in range(1, len(prices)):
            #print(profit)
            #print(type(max_till_now))
            if prices[i] < max_till_now:
                profit += max_till_now - min_till_now
                max_till_now=prices[i]
                min_till_now = prices[i]
            else:
                max_till_now = max(max_till_now, prices[i])
                min_till_now = min(min_till_now, prices[i])
        if profit == 0 and prices[-1] > prices[0]:
            profit = prices[-1] - prices[0]
        #print(prices)
        return profit
sol = Solution()


def onePass(prices):
    max_profit = 0
    for i in range(len(prices)):
        if prices[i] > prices[i-1]:
            max_profit += prices[i] - prices[i-1]
    return max_profit

prices = [7, 1, 5, 3, 6, 4]
print(7)
print(sol.maxProfit(prices))


prices = [1,2,3,4,5]
print(4)
print(onePass(prices))

prices = [7,6,4,3,1]
print(0)
print(sol.maxProfit(prices))