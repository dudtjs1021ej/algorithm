import sys
# 배열을 입력받아 자신을 제외한 나머지 모든 요소가 곱한 값으로 리턴
# 나눗셈을 하지않고 O(n)에 풀이해야 함

def productExceptSelf(self, nums):
    out = []
    p = 1

    #왼쪽 곱셈
    for i in range(0, len(nums)):
        out.append(p)
        p = p *nums[i]

    p = 1
     # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
    for i in range(len(nums) - 1, 0 - 1, -1):
        out[i] = out[i] * p
        p = p* nums[i]