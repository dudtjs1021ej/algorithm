import sys
# 배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라
# 풀이2 - 투 포인터로 합 계산
def threeSum(self, nums):
    results = []
    nums.sort()

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]: # 중복된 값은 건너뛰기
            continue

        left, right = i+1, len(nums)-1 #left는 i앞 right는 맨 뒤
        sum = nums[i] + nums[left] + nums[right]
        if sum < 0:
            left += 1
        elif sum > 0 :
            right -= 1
        else: #합이 0인 경우
            results.append[nums[i],nums[left],nums[right]] #result에 정답을 넣음

            # 중복을 피하기 위해 left right 양 옆으로 같은 숫자가 나오면 넘김
            while left < right and nums[left] == nums[left+1]:
                left += 1
            while left < right and nums[right] == nums[right-1]:
                right -= 1
            left += 1 
            right -= 1