from typing import List
# 겹치는 구간을 병합하라.
# [[1,3], [2,6], [8,10]] -> [[1,6], [8,10]]

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]: 
        merged = []
        for i in sorted(intervals, key=lambda x: x[0]): # 첫번째값을 기준으로 정렬
            if merged and i[0] <= merged[-1][1]: # 시작값이 이전 아이템의 끝값과 겹치면 병합
                merged[-1][1] = max(merged[-1][1], i[1])
            else:
                merged += i, # 안겹치면 새로운 아이템 추가
        return merged