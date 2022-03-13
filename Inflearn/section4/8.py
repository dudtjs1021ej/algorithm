# 구명보트는 2명 이하로만 탈 수 있으며, 
# 보트 한 개에 탈 수 있는 총 무게도 M kg 이하로 제한되어 있습니다.
# N명의 승객 몸무게가 주어졌을 때 승객 모두가 탈출하기 위한 구명보트의 최소개수를 출력하는 프로그램을 작성하세요.
import sys
from collections import deque
n, m = map(int, input().split())
weights = list(map(int, input().split()))
weights.sort()
weights = deque(weights) # 데크로 변경
count = 0
while weights:
    if len(weights) == 1:
        count += 1
        break
    if weights[0] + weights[-1] > m: # 젤 가벼운사람+무거운사람이 한계를 넘어서면
        weights.pop() # 가장 무거운 사람만 탈출
        count += 1
    else: # 둘 다 탈출할 수 있으면
        weights.pop()
        weights.popleft() # deque의 맨 앞 pop
        count += 1

# 후기
#   내림차순으로 정렬하고 m-선택한 몸무게 구하고, 
#   그 값보다 작은 몸무게가 있는지 차례대로 비교하며 선택하며 풀었다. -> 이중포문으로 비효울적
#   가장가벼운사람 + 가장무거운사람(정렬 후 맨 앞, 맨 뒤)만 비교하면 되었었다.
# 새로 배운 점
#   deque : list는 pop하고 모두 땡겨줘야돼서 비효율적이지만 deque는 포인터만 변경하면돼서 효율적
#   popleft()로 맨 앞 pop


        
