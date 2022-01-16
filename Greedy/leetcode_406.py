import heapq
from typing import List
# (h,k) -> h는 키, k는 나보다 키 큰 사람 수
# 키에 따른 대기열 구성 -> 우선순위큐 이용

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []
        # 키 역순, 인덱스 삽입
        for person in people:
            heapq.heappush(heap, (-person[0], person[1])) # 최소힙

        result = []
        # 키 역순, 인덱스 추출
        while heap:
            person = heapq.heappop(heap)
            result.insert(person[1], [-person[0], person[1]])
        return result