
# 연결 리스트를 삽입 정렬로 정렬하라.
# >head = 정렬해야 할 대상, cur = 정렬을 끝낸 대상

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        cur = parent = ListNode(None)
        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next

            cur.next, head.next, head = head, cur.next, head.next

            cur = parent
        return cur.next