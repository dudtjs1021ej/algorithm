from typing import List
# 딱 하나를 제외하고 모든 엘리먼트는 2개씩 있다.
# 1개인 엘리먼트를 찾아라.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num # XOR -> result로 남는 건 1개인 엘리먼트

        return result