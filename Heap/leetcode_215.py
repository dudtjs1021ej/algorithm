import heapq
from typing import List
# 정렬되지 않은 배열에서 k번째로 큰 요소를 추출하라.

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = list()
        for n in nums:
            heapq.heappush(heap, -n) # 파이썬 heapq모듈 최소힙(가장 작은 값이 맨 위)만 지원 -> 음수로 저장

        # heapq.heapify(nums) # 푸시 안해도 한번에 처리 가능 

        for _ in range(1, k):
            heapq.heappop(heap)

        return -heapq.heappop(heap)