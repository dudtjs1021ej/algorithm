# 1부터 N까지의 모든 자연수로 구성된 길이 N의 수열이 주어집니다.
# 이 수열의 왼쪽 맨 끝 숫자 또는 오른쪽 맨 끝 숫자 중 하나를 가져와 나열하여 가장 긴 증가수열을 만듭니다.
# 이때 수열에서 가져온 숫자(왼쪽 맨 끝 또는 오른쪽 맨 끝)는 그 수열에서 제거됩니다.
import sys
n = int(input())
a = list(map(int, input().split()))
left = 0
right = n-1
last = 0
res = ""
tmp = []
while left<=right:
    if a[left] > last:
        tmp.append((a[left], "L"))
    if a[right] > last:
        tmp.append((a[right],"R"))
    if len(tmp) == 0:
        break
    tmp.sort()
    res = res+tmp[0][1]
    last = tmp[0][0]
    if tmp[0][1] == "R":
        right -= 1
    else:
        left += 1
    tmp.clear()
print(len(res))
print(res)

# 후기
# 왼오 중 더 작은 것 선택하고, 그 다음 왼오 중 전 선택보다 큰 값 선택하는 방식으로 풀이