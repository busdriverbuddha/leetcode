class Solution:
    def intToRoman(self, num: int) -> str:
        eqs = [
            [1000, "M"],
            [900, "CM"],
            [500, "D"],
            [400, "CD"],
            [100, "C"],
            [90, "XC"],
            [50, "L"],
            [40, "XL"],
            [10, "X"],
            [9, "IX"],
            [5, "V"],
            [4, "IV"],
            [1, "I"],
        ]
        s = ""
        for val, text in eqs:
            if val > num:
                continue
            q, num = divmod(num, val)
            s += text * q
            if num == 0:
                break
        return s


test_cases = [
    [3749, "MMMDCCXLIX"],
    [58, "LVIII"],
]

s = Solution()

for i, (test_in, test_out) in enumerate(test_cases, 1):
    print(f"Case {i}: ", end="")
    a = s.intToRoman(test_in)
    if a == test_out:
        print("Passed.")
    else:
        print(f"Expected {test_out}; got {a}.")
