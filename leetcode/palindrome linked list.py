class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q = []
        node = head

        while node is not None:
            q.append(node.val)
            node = node.next

        for i in range(len(q) // 2):
            if q[i] != q[-(i + 1)]:
                return False

        return True
