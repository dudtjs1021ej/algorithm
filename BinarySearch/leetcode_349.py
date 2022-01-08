import bisect
from typing import List, Set
# 두 배열의 교집합을 구하라.

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result: Set = set()
        nums2.sort()
        for n1 in nums1:
            # 이진 검색으로 일치 여부 판별
            i2 = bisect.bisect_left(nums2, n1) # 리턴한 인덱스의 왼쪽에 삽입
            if len(nums2) > 0 and len(nums2) > i2 and n1 == nums2[i2]: # 리턴한 인덱스와 같은 값이면 교집합
                result.add(n1)

        return 