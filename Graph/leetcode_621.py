import collections
from typing import List
# 모든 테스크를 실행하기 위한 최소 간격을 구하라.
# n번 간격내에서 같은 테스크 실행 못함

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        result = 0

        while True:
            sub_count = 0
            # 개수 순 추출
            for task, _ in counter.most_common(n + 1): # 가장 개수가 많은 아이템 n+1개
                sub_count += 1 
                result += 1

                counter.subtract(task) # 1개씩 개수 제거하는 함수
                # 0 이하인 아이템을 목록에서 완전히 제거
                counter += collections.Counter()

            if not counter:
                break

            result += n - sub_count + 1

        return result