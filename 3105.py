class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if 0 <= len(nums) <= 1:
            return len(nums)

        # by default, the longest subarray will be [0,0] unless proven otherwise
        l_asc = r_asc = 0
        l_desc = r_desc = 0

        l_a = 0
        for r_a in range(1, len(nums)):
            if nums[r_a] > nums[r_a - 1]:
                if r_a - l_a > r_asc - l_asc:
                    l_asc, r_asc = l_a, r_a
            else:
                l_a = r_a

        l_d = 0
        for r_d in range(1, len(nums)):
            if nums[r_d] < nums[r_d - 1]:
                if r_d - l_d > r_desc - l_desc:
                    l_desc, r_desc = l_d, r_d
            else:
                l_d = r_d

        return max(r_desc - l_desc + 1, r_asc - l_asc + 1)


test_cases = [
    [],
    [1],
    [1, 4, 3, 3, 2],
    [3, 3, 3, 3],
    [3, 2, 1],
    [1, 3],
]

expected_answers = [
    0,
    1,
    2,
    1,
    3,
    2,
]

s = Solution()
for case, answer in zip(test_cases, expected_answers):
    a = s.longestMonotonicSubarray(case)
    if a != answer:
        print(f"For input: {case}")
        print(f"Expected: {answer}")
        print(f"Got: {a}")
        print()
