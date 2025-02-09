class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        period = 2 * numRows - 2
        r = s[::period]
        for i in range(1, numRows - 1):
            k = 0
            while True:
                try:
                    r += s[i + k * period]
                except IndexError:
                    break
                try:
                    r += s[i + (k + 1) * period - 2 * i]
                except IndexError:
                    break
                k += 1
        r += s[numRows - 1::period]
        return r


cases = [
    [("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR"],
    [("PAYPALISHIRING", 4), "PINALSIGYAHRPI"],
    [("A", 1), "A"]
]

sol = Solution()

for i, ((s, numRows), expected_output) in enumerate(cases, 1):
    print(f"Case {i:02d}:")
    a = sol.convert(s, numRows)
    if a == expected_output:
        print("Passed.")
    else:
        print(f"Expected: {expected_output}. Got: {a}")
