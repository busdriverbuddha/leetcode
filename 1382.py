from typing import Optional


# TODO: improve speed
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_level_order(cls, arr):
        if not arr or arr[0] is None:
            return None

        root = cls(arr[0])
        queue = [root]
        i = 1
        while i < len(arr):
            node = queue.pop(0)
            # Process left child
            if i < len(arr):
                if arr[i] is not None:
                    node.left = cls(arr[i])
                    queue.append(node.left)
                i += 1
            # Process right child
            if i < len(arr):
                if arr[i] is not None:
                    node.right = cls(arr[i])
                    queue.append(node.right)
                i += 1
        return root


class Solution:

    def is_balanced(self, root):
        def check(node):
            if not node:
                return 0
            left_height = check(node.left)
            if left_height == -1:
                return -1
            right_height = check(node.right)
            if right_height == -1:
                return -1
            if abs(left_height - right_height) > 1:
                return -1
            return max(left_height, right_height) + 1

        return check(root) != -1

    def middle_index(self, left, right):  # python slicing
        if right - left <= 2:
            return left
        if (right - left) % 2 == 1:
            return left + (right - left) // 2
        else:
            return left + (right - left) // 2 - 1

    def _inorder(self, root, sorted_nodes):
        if root.left is not None:
            self._inorder(root.left, sorted_nodes)
        sorted_nodes.append(root.val)
        if root.right is not None:
            self._inorder(root.right, sorted_nodes)

    def balance_subtree(self, sorted_nodes, start, end):
        middle = self.middle_index(start, end)

        left_child = right_child = None

        if sorted_nodes[start:middle]:
            left_child = self.balance_subtree(sorted_nodes, start, middle)

        if sorted_nodes[middle + 1:end]:
            right_child = self.balance_subtree(sorted_nodes, middle + 1, end)

        return TreeNode(
            val=sorted_nodes[middle],
            left=left_child,
            right=right_child
        )

    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if self.is_balanced(root):
            return root

        sorted_nodes = []
        self._inorder(root, sorted_nodes)

        return self.balance_subtree(sorted_nodes, 0, len(sorted_nodes))


inputs = [
    [1, None, 2, None, 3, None, 4, None, None],
    [2, 1, 3],
    [5, 3, 10, 2, 4, 8, 15, None, None, None, None,
     None, 9, 14, 20,
     None, None, 13, None, 17, None, None, None, None, None]
]

s = Solution()

for i, input_instance in enumerate(inputs, 1):
    root = TreeNode.from_level_order(input_instance)
    this_output = s.balanceBST(root)
    if not this_output or not s.is_balanced(this_output):
        print(f"Case {i}: Fail.")
    else:
        print(f"Case {i}: Pass.")
