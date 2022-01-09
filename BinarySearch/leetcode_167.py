from typing import List
import bisect
# 정렬된 배열을 받아 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.
# 배열의 인덱스는 1부터 시작함

class Solution:
    # 이진 검색
    def twoSum1(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            left, right = k + 1, len(numbers) - 1
            expected = target - v 
            # 이진 검색으로 나머지 값 판별
            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] < expected:
                    left = mid + 1
                elif numbers[mid] > expected:
                    right = mid - 1
                else:
                    return k + 1, mid + 1 # 인덱스는 1부터 시작

    # bisect모듈 사용 + 슬라이싱 최소화
    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            expected = target - v
            nums = numbers[k + 1:]
            i = bisect.bisect_left(nums, expected)
            if i < len(nums) and numbers[i + k + 1] == expected:
                return k + 1, i + k + 2

