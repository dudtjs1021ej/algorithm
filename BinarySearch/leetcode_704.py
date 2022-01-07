from typing import List
# 정렬된 nums를 받아 이진 검색으로 target에 해당하는 인덱스를 찾아라.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2 # 왼쪽~오른쪽의 가운데 인덱스

            if nums[mid] < target: # 타겟보다 작으면
                left = mid + 1 # 왼쪽을 mid+1 로 이동
            elif nums[mid] > target: # 타겟보다 크면
                right = mid - 1 # 오른쪽을 mid-1 로 이동
            else:
                return mid
        return -1