class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        l = 0
        diff_max = 0
        for r in range(n):
            if prices[r] - prices[l] > diff_max:
                diff_max = prices[r] - prices[l]
            elif prices[l] > prices[r]:
                l = r
        return diff_max

if __name__ == "__main__":
    s = Solution()
    prices = [7,1,5,3,6,4]
    print(s.maxProfit(prices))
    prices = [7,6,4,3,1]
    print(s.maxProfit(prices))