# 채점 1011100110
# 점수 1012300120 -> 10
import sys
# 새로운 점수 리스트에 점수들 넣어서 sum(score)로 계산
def mySoultion(): 
    n = int(input())
    grades = list(map(int, input().split()))
    scores = []
    score = 1
    for i in grades:
        if i == 0:
            scores.append(i)
            score = 1
        elif i == 1:
            scores.append(score)
            score += 1
    print(sum(scores))

# 바로 sum 계산
def answer():
    n = int(input())
    a = list(map(int, input().split()))
    sum = 0
    cnt = 0
    for x in a:
        if x == 1:
            cnt += 1
            sum += cnt
        else:
            cnt = 0
# 후기
# 굳이 점수 리스트 하나 더 만들 필요없이 바로 sum 계산하면 됐었음.

