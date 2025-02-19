from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        def search_left(nums, target):
            i, j = 0, len(nums)

            while i < j:
                m = (i + j) // 2
                if target > nums[m]:
                    i = m + 1
                else:
                    j = m

            return i

        left = search_left(nums, target)
        right = search_left(nums, target + 1)

        if left == right or nums[left] != target or nums[right - 1] != target:
            return [-1, -1]

        return [left, right - 1]


test_cases = [
    (([5, 7, 7, 8, 8, 10], 8), [3, 4]),
    (([5, 7, 7, 8, 8, 10], 6), [-1, -1]),
    (([], 0), [-1, -1]),
    (([2, 2], 3), [-1, -1]),
]

s = Solution()

for i, (test_in, test_out) in enumerate(test_cases, 1):
    nums, target = test_in
    out = s.searchRange(nums, target)
    if out == test_out:
        print(f"Case {i}: passed.")
    else:
        print(f"Case {i}: expected {test_out}, got {out}")
