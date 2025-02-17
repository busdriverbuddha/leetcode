class Solution:

    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a, b = b, a

        i = len(a) - 1
        j = len(b) - 1
        res = ""
        acc = 0
        while i >= 0 and j >= 0:
            acc, d = divmod(int(a[i], 2) + int(b[j], 2) + acc, 2)
            res = str(d) + res
            i -= 1
            j -= 1
        while i >= 0:
            acc, d = divmod(int(a[i], 2) + acc, 2)
            res = str(d) + res
            i -= 1
        res = str(acc) + res
        if "1" not in res:
            return "0"
        return res.lstrip("0")


s = Solution()

test_cases = [
    (("11", "1"), "100"),
    (("1010", "1011"), "10101"),
]

for i, (test_in, test_out) in enumerate(test_cases, 1):
    print(f"Case {i}: ", end="")
    ans = s.addBinary(*test_in)
    if ans == test_out:
        print("Passed.")
    else:
        print(f"Got {ans}; expected {test_out}.")
