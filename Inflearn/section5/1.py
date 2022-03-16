# 선생님은 현수에게 숫자 하나를 주고, 해당 숫자의 자릿수들 중 m개의 숫자를 제거하 여 가장 큰 수를 만들라고 했습니다. 
# 여러분이 현수를 도와주세요.(단 숫자의 순서는 유지해야 합니다)
# 스택으로 구현
import sys
from collections import deque
n ,m = map(int, input().split())
num = list(map(int, str(n))) # 숫자 하나하나를 리스트로 넣음
stack = []
for x in num:
    while stack and m>0 and stack[-1]<x: # 스택이 비어있지않고 젤 뒤에값이 나보다 작으면 pop
        stack.pop()
        m -= 1
    stack.append(x)
if m != 0:
    stack = stack[:-m] # 더 지울 수 있다면 현재 무조건 오름차순 정렬이므로 뒤에부터 지움
res = ''.join(map(str, stack)) # 붙여서 출력

# 후기
# 스택에 넣으면서 제일 위에값이 넣을값보다 작으면 pop하는 식으로 풀이
# ''.join -> 붙여서 정렬 / stack[:-2] 뒤에 2개 제외
