from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        mi = float('inf')
        for v in prices:
            if v - mi > ans:
                ans = v - mi
            if v < mi:
                mi = v

        return max(0, ans)


test_cases = [
    [[7, 1, 5, 3, 6, 4], 5],
    [[7, 6, 4, 3, 1], 0],
    [[2, 1, 2, 1, 0, 1, 2], 2],
    [[3, 3, 5, 0, 0, 3, 1, 4], 4],
]

s = Solution()

k = 1
for prices, max_profit in test_cases:
    ans = s.maxProfit(prices)
    if ans == max_profit:
        print(f"Case {k}: passed.")
    else:
        print(f"Case {k}: got {ans}, expected {max_profit}.")
    k += 1
