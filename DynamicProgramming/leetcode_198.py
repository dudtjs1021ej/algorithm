import collections
from typing import List
# 옆집은 못터는 집 도둑

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        dp = collections.OrderedDict() # 입력 순서 유지
        dp[0], dp[1] = nums[0], max(nums[0], nums[1]) 
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i]) # 더 큰 값 누적하며 저장

        return dp.popitem()[1] # 마지막 아이템의 value pop