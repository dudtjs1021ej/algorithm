from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 모든 주유소 방문 가능 여부 판별
        if sum(gas) < sum(cost): # 전체 기름양보다 비용이 더 많이들면 무조건 실패
            return -1

        start, fuel = 0, 0
        for i in range(len(gas)):
            # 출발점이 안되는 지점 판별
            if gas[i] + fuel < cost[i]: # 비용이 더 많이 들 경우
                start = i + 1
                fuel = 0
            else: # 이동 가능한 경우
                fuel += gas[i] - cost[i]
        return start