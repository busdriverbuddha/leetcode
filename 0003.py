class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import defaultdict

        if len(s) == 0:
            return 0

        k = l = 0
        maxlen = 1
        seen = defaultdict(bool)
        seen[s[0]] = True

        for l in range(1, len(s)):
            if not seen[s[l]]:
                seen[s[l]] = True
                if l - k + 1 > maxlen:
                    maxlen = l - k + 1
            else:
                while seen[s[l]] and k <= l:
                    seen[s[k]] = False
                    k += 1
                seen[s[l]] = True

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
