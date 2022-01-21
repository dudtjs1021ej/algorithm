from typing import List
# 연속 서브 배열 최대합 리턴

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)): 
            nums[i] += nums[i - 1] if nums[i - 1] > 0 else 0 # 이전값이 0이하면 0으로 초기화, 0이상이면 누적 합
        return max(nums)