# 공주 구하기(큐 자료구조로 해결)
import sys
from collections import deque

n, k = map(int, input().split())
a = list(range(1, n+1))
a = deque(a)
count = 0
while a:
    for _ in range(k-1): # k-1까지 pop하고 append
        a.append(a.popleft())
    a.popleft()
    if len(a) == 1: # 하나 남았을 때 -> 답 출력
        print(a[0])
        a.popleft()

# 후기
# 회전하는 큐 구현 -> popleft한 값 바로 뒤에 append
# 빼야할것은 popleft만하고 append 하지않음
