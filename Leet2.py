def maxProfit(prices):

    l, r = 0, 1

    maxProf = 0

    while r < len(prices):
        if prices[r] < prices[l]:
            profit = prices[r] - prices[l]

            maxProf = max(profit, maxProf)

        else:
            l = r
        r += 1
    return maxProf