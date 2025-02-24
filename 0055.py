from typing import List

from Checker import Checker


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i, v in enumerate(nums):
            if i > max_reach:
                return False
            if i + v > max_reach:
                max_reach = i + v
        return True


test_in_kwargs = [
    {'nums': [2, 3, 1, 1, 4]},
    {'nums': [3, 2, 1, 0, 4]},
]

test_out = [
    True,
    False
]

s = Solution()
c = Checker(s.canJump, test_in_kwargs, test_out)
c.check()
