# 최소힙
import sys
import heapq as hq

a = []
while True:
    n = int(input())
    if n == -1:
        break
    elif n == 0: # heappop
        if len(a) == 0: # 비어있으면
            print("-1")
        else:
            print(hq.heappop(a))

    else: #heappush
        hq.heappush(a, n)

# 최소힙 개념 알아야함
