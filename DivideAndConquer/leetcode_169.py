import collections
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]

        half = len(nums) // 2
        a = self.majorityElement(nums[:half]) # 반씩 분할
        b = self.majorityElement(nums[half:])

        return [b, a][nums.count(a) > half] # 과반수 리턴