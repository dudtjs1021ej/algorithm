# 연결리스트를 O(nlogn)에 정렬해라

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

 # 병합 정렬
class Solution:
    # 두 정렬 리스트 병합
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 크기를 비교해 이어붙임
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)

        return l1 or l2

    def sortList(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head

        # 런너 기법 활용
        half, slow, fast = None, head, head

        #fast를 끝까지 이동 -> slow는 중앙에 도착, half는 slow 바로 전
        while fast and fast.next: 
            half, slow, fast = slow, slow.next, fast.next.next
        half.next = None

        # 분할 재귀 호출
        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        return self.mergeTwoLists(l1, l2)