# N명의 대기목록 순서의 환자 위험도가 주어지면, 
# 대기목록상의 M번째 환자는 몇 번째로 진료 를 받는지 출력하는 프로그램을 작성하세요.
import sys
from collections import deque
n, m = map(int, input().split())
patient = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
patient = deque(patient)
count = 0
while True:
    cur = patient.popleft()
    if any(cur[1] < x[1] for x in patient): # 하나라도 맨 앞보다 위험도가 크면
        patient.append(cur)
    else:
        count += 1
        if cur[0] == m:
            break
print(count)

# 후기
# 특정 환자가 몇번째로 빠지는지 풀 때, 그 환자의 index를 enumerate 사용해 튜플로 저장
# 현재 빠진 환자의 cur[0]와 특정 환자의 인덱스가 같으면 정답
