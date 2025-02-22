class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        f = [1] * m
        for _ in range(1, n):
            for j in range(1, m):
                f[j] += f[j - 1]
        return f[-1]


test_cases = [
    [(3, 7), 28],
    [(3, 2), 3],
]

s = Solution()

for i, (test_in, test_out) in enumerate(test_cases, 1):
    print(f"Case {i}:", end="")
    ans = s.uniquePaths(*test_in)
    if ans == test_out:
        print("passed.")
    else:
        print(f"expected {test_out}; got {ans}")
