# DVD의 최소 용량 크기를 출력하세요. -> 이분탐색 사용
import sys
n, m = map(int, input().split())
sizes = list(map(int, input().split()))
left = 1
right = sum(sizes)
res = 0
while left <= right:
    mid = (left+right) // 2
    sum = 0 # 그룹의 총 합
    count = 1 # 그룹의 수
    for x in sizes:
        if sum + x > mid:
            count += 1
            sum = x
        else:
            sum += x
    if count <= m:
        res = mid
        right = mid - 1
    else:
        left = mid + 1
print(res)

# 후기
# 함수로 구현한 것 제외하고 똑같이 풀었다.
# 이분탐색으로 용량을 구함