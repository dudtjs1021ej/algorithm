import heapq
from typing import List
# pointd 목록이 있을 때, 원점에서 가장 가까운 점 k개를 출력하라.

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for (x, y) in points:
            dist = x ** 2 + y ** 2

            # 우선순위큐 -> heapq모듈 사용 -> 최소힙이기때문에 적합
            heapq.heappush(heap, (dist, x, y)) 

        result = []
        for _ in range(K):
            (dist, x, y) = heapq.heappop(heap)
            result.append((x, y))
        return result