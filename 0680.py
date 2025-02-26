from Checker import Checker


class Solution:
    def validPalindrome(self, s: str) -> bool:

        def checkPalindrome(s: str) -> bool:
            if len(s) == 1:
                return True

            start = 0
            end = len(s) - 1
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1

            return True

        if len(s) == 1:
            return True

        start = 0
        end = len(s) - 1

        while start < end:
            if s[start] != s[end]:
                return checkPalindrome(s[start + 1:end + 1]) or checkPalindrome(s[start:end])
            start += 1
            end -= 1

        return True


test_in_kwargs = [
    dict(s="aba"),
    dict(s="abca"),
    dict(s="abc"),
    dict(s="aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"),
    dict(s="acxcybycxcxa")
]

test_out = [
    True,
    True,
    False,
    True,
    True,
]

s = Solution()
c = Checker(
    testing_function=s.validPalindrome,
    test_in_kwargs=test_in_kwargs,
    test_out=test_out
)
c.check()
