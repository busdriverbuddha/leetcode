class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def to_list(self):
        """Exports the tree to a list in level order (rank order) representation."""
        result = []
        queue = [self]
        while queue:
            node = queue.pop(0)
            if node is not None:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)
        # Remove trailing None values for a cleaner representation.
        while result and result[-1] is None:
            result.pop()
        return result

    @classmethod
    def from_list(cls, lst):
        """Generates a tree from a list in level order (rank order) representation."""
        if not lst:
            return None
        root = cls(lst[0])
        queue = [root]
        i = 1
        while queue and i < len(lst):
            current = queue.pop(0)
            # Assign left child
            if i < len(lst):
                if lst[i] is not None:
                    current.left = cls(lst[i])
                    queue.append(current.left)
                i += 1
            # Assign right child
            if i < len(lst):
                if lst[i] is not None:
                    current.right = cls(lst[i])
                    queue.append(current.right)
                i += 1
        return root
