from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        best = 1e9

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                this_sum = nums[i] + nums[left] + nums[right]

                if this_sum == target:
                    return this_sum

                if abs(this_sum - target) < abs(best - target):
                    best = this_sum

                if this_sum < target:
                    left += 1
                else:
                    right -= 1

        return best
