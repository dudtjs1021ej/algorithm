import sys
import heapq
# k개의 정렬된 리스트를 1개의 정렬된 리스트로 병합하라
# 우선순위 큐를 이용
class Solution:
    def mergeKLists(self, lists):
        root = result = ListNode(None)
        heap = []
        
        # 각 연결리스트의 루트를 힙에 저장
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i])) #에러 방지를 위해 item 수정
                
        # 힙 추출 이후 다음 노드는 다시 저장
        while heap:
            node = heapq.heappop(heap) # list.val 가 작은 순서대로 pop
            
            idx = node[1]
            result.next = node[2]
            
            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next)) # 그 다음 노드는 다시 힙에 저장
                
        return root.next
            
        