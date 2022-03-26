# 필수과목순서가 주어지면 현수가 짠 N개의 수업설계가 잘된 것이면 “YES", 
# 잘못된 것이면 ”NO“를 출력하는 프로그램을 작성하세요.
import collections
import sys
from collections import deque
order = list(input())
n = int(input())
for i in range(n):
    dq = deque(order)
    plan = list(input())
    for x in plan:   
        if x in dq:
            if x != dq.popleft():
                print("#%d NO" %(i+1))
                break
    else:
        if len(dq) == 0:
            print("#%d YES" %(i+1))
        else:
            print("#%d NO" %(i+1))

# 후기
# 거의 비슷하게 접근
# 대신 현재 문자가 순서에 있는지 체크하지 않음(x in dq) (모든 문자 검사)

