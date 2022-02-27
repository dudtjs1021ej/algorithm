# 임의의 N개의 숫자가 입력으로 주어집니다. 
# N개의 수를 오름차순으로 정렬한 다음 N개의 수 중 한 개의 수인 M이 주어지면 
# 이분검색으로 M이 정렬된 상태에서 몇 번째에 있는지 구하는 프로그램을 작성하세요. 
# 단 중복값은 존재하지 않습니다.
import sys
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
left = 0
right = n-1

while left <= right:
    mid = (left+right) // 2
    if a[mid] == m:
        break
    elif a[mid] < m:
        left = mid+1
    else:
        right = mid-1
print(mid+1)

# 후기
# 똑같이 풀었다.
# 이분탐색 : 왼쪽, 오른쪽 포인터 주고 가운데값과 비교해서 포인터 이동
