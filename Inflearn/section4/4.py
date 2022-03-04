# 첫 줄에 가장 가까운 두 말의 최대 거리를 출력하세요. -> 이분탐색
import sys
# 배치할 수 있는 마리 수 리턴
def Count(len):
    cnt = 1
    ep = line[0] # 첫번째 마굿간에 첫번쨰 말 배치
    for i in range(1,n):
        if line[i] - ep >= len: # 거리 측정
            cnt += 1 # 말 배치
            ep = line[i]
    return cnt


n, c = map(int, input().split())
line = []
for _ in range(n):
    tmp = int(input())
    line.append(tmp)
line.sort()
lt = 1
rt = line[n-1] # max값
while lt <= rt:
    mid = (lt+rt) // 2
    if Count(mid) >= c:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

# 후기
# 어려워서 강의 봄.
# 말 배치하는 법  
# -> 첫번째 마굿간에 무조건 한마리 배치하고
#    그 다음 말과의 거리 비교하며 일정 거리 이상하면 말 배치하는 방식

