from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        positions = {mat[i][j]: (i, j) for i in range(n) for j in range(m)}
        col_counts = [0] * m
        row_counts = [0] * n
        for i, val in enumerate(arr):
            u, v = positions[val]
            row_counts[u] += 1
            col_counts[v] += 1
            if row_counts[u] == m or col_counts[v] == n:
                return i


ins = [
    {
        'arr': [1, 3, 4, 2],
        'mat': [[1, 4], [2, 3]]
    },
    {
        'arr': [2, 8, 7, 4, 1, 3, 5, 6, 9],
        'mat': [[3, 2, 5], [1, 4, 6], [8, 7, 9]]
    }
]

outs = [2, 3]
s = Solution()
for i, (input_instance, output_instance) in enumerate(zip(ins, outs), 1):
    this_solution = s.firstCompleteIndex(arr=input_instance['arr'], mat=input_instance['mat'])
    print(f"Case {i}:")
    if this_solution == output_instance:
        print("Passed.")

    else:
        print(f"Expected: {output_instance}. Got: {this_solution}")

    print()
