from typing import List
# 항목들을 조합하여 가장 큰 수를 출력하라
# [10,2] -> 210

class Solution:
    # 문제에 적합한 비교 함수
    @staticmethod 
    #9, 30 -> 930이큰지 309가 큰지 비교
    def to_swap(n1: int, n2: int) -> bool:
        return str(n1) + str(n2) < str(n2) + str(n1)

    # 삽입 정렬 구현
    def largestNumber(self, nums: List[int]) -> str:
        i = 1
        while i < len(nums):
            j = i
            while j > 0 and self.to_swap(nums[j - 1], nums[j]): 
                nums[j], nums[j - 1] = nums[j - 1], nums[j] # swap한 값이 더 크면 swap
                j -= 1
            i += 1

        return str(int(''.join(map(str, nums)))) 