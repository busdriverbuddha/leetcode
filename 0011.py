from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = -1

        while left < right:
            h_l, h_r = height[left], height[right]
            area = min(h_l, h_r) * (right - left)
            if area > max_area:
                max_area = area
            if h_l == h_r:
                left += 1
                right -= 1
            elif h_l < h_r:
                left += 1
            else:
                right -= 1

        return max_area


s = Solution()

test_cases = [
    [[1, 8, 6, 2, 5, 4, 8, 3, 7], 49],
    [[1, 1], 1],
]

for i, (test_in, test_out) in enumerate(test_cases, 1):
    out = s.maxArea(test_in)
    if out == test_out:
        print(f"Case {i}: passed.")
    else:
        print(f"Case {i}: expected {test_out}, got {out}.")
