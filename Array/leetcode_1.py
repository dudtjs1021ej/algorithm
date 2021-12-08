import sys
# 덧셈을 해 타겟을 만들 수 있는 배열의 두 숫자의 인덱스를 리턴하라

# ----풀이3 : 딕셔너리 사용
def twoSum(self, nums, target: int):
    nums_map = {} # 딕셔너리
    for i, num in enumerate(nums): 
        nums_map[num] = i # num를 key로, 인덱스를 value으로 딕셔너리에 저장
        
    for i, num in enumerate(nums):
        # 타겟에서 첫 번째 수를 뺀 결과가 있고 같은 인덱스가 아니라면 두 숫자 인덱스 리턴
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]


# 투포인터 사용은 정렬을 해야하기 때문에 인덱스를 리턴하지 않는 문제에 사용

