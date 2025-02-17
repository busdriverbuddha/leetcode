class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        left = right = 0
        maxlen = 1
        seen = [False] * 128
        seen[ord(s[0])] = True

        for right in range(1, len(s)):
            if not seen[ord(s[right])]:
                seen[ord(s[right])] = True
                if right - left + 1 > maxlen:
                    maxlen = right - left + 1
            else:
                while seen[ord(s[right])] and left <= right:
                    seen[ord(s[left])] = False
                    left += 1
                seen[ord(s[right])] = True

        return maxlen


test_cases = [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
]

s = Solution()

for i, (test_in, test_out) in enumerate(test_cases, 1):
    print(f"Case {i}: ", end="")
    a = s.lengthOfLongestSubstring(test_in)
    if a == test_out:
        print("Passed.")
    else:
        print(f"Expected {test_out}; got {a}.")
