class Solution:
    def finalPrices(self, prices):
        r = [0] * len(prices)
        for i in range(len(prices)):
            newPrice = prices[i]
            for j in range(i+1, len(prices)):
                if prices[j] <= prices[i]:
                    newPrice -= prices[j]
                    break
            r[i] = newPrice
        return r