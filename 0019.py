# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, values: list) -> "ListNode":
        head = cls(values[0])
        p = head
        for v in values[1:]:
            p.next = cls(v)
            p = p.next
        return head

    def to_list(self) -> list[int]:
        p = self
        values = []
        while p is not None:
            values.append(p.val)
            p = p.next
        return values


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy: ListNode = ListNode()
        dummy.next = head
        first: ListNode = dummy
        second: ListNode = dummy

        for _ in range(n + 1):
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next

        return dummy.next


s = Solution()

test_cases = [
    [
        [[1, 2, 3, 4, 5], 2],
        [1, 2, 3, 5]
    ],
    [[[1], 1], []],
    [[[1, 2], 1], [1]],
]

for i, (test_in, test_out) in enumerate(test_cases, 1):
    values, n = test_in
    head_in = ListNode.from_list(values)
    head_out = s.removeNthFromEnd(head_in, n)
    values_out = head_out.to_list() if head_out else []
    if values_out == test_out:
        print(f"Case {i}: passed.")
    else:
        print(f"Case {i}: expected {test_out}, got {values_out}.")
