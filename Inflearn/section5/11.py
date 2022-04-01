# 최대힙
import sys
import heapq as hq
a = []
while True:
    n = int(input())
    if n == -1:
        break
    elif n == 0: # pop
        if len(a) == 0:
            print("-1")
        else:
            print(-hq.heappop(a))
    else: # push
        hq.heappush(a, -n)

# 최대힙 -> 내장함수는 최소힙만 지원하기때문에 push할때 마이너스를 붙여서 넣음



