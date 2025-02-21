from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        combs = list(mapping[digits[0]])

        for d in digits[1:]:
            combs = [
                c + lt
                for c in combs
                for lt in mapping[d]
            ]

        return combs


test_cases = [
    "23",
    "",
    "2",
]

s = Solution()

for digits in test_cases:
    print(digits, s.letterCombinations(digits))
