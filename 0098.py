from typing import Optional

from TreeNode import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def check(node, low=float('-inf'), high=float('inf')):
            if not low < node.val < high:
                return False

            if node.right and not check(node.right, node.val, high):
                return False

            if node.left and not check(node.left, low, node.val):
                return False

            return True

        return check(root)


test_cases = [
    [[2, 1, 3], True],
    [[5, 1, 4, None, None, 3, 6], False],
    [[2, 2, 2], False],
]

s = Solution()

for i, (test_in, test_out) in enumerate(test_cases, 1):
    print(f"Case {i}: ", end="")
    root = TreeNode.from_list(test_in)
    ans = s.isValidBST(root)
    if ans == test_out:
        print("passed.")
    else:
        print(f"expected {test_out}, got {ans}.")
