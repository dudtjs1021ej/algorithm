# 대표값
import sys

# 선수 강의 - 최솟값 구하기
arr = [5,3,7,9,2,5,2,6]
arrMin = float('inf') # 가질 수 있는 가장 큰 값
for x in arr:
    if x < arrMin:
        arrMin = x

def mySolution():
    n = int(input())
    scores = list(map(int, input().split()))
    sum = 0
    for score in scores:
        sum += score
    avg = round((sum / n)) # 소수점 첫째자리 반올림

    sort_scores = scores[:]
    # 정렬된 점수 리스트를 만들어서 평균 삽입 
    sort_scores.append(avg)
    sort_scores.sort()

    # 딱 평균인 학생이 있는 경우 (= 평균을 삽입한 상태에서 평균과 같은 값을 가진게 1이상인경우)
    if (sort_scores.count(avg) > 1): 
        print(scores.index(avg) + 1)

    # 평균인 학생 없을 경우 
    else:
        avg_index = sort_scores.index(avg)
        front_avg = sort_scores[avg_index+1] 
        back_avg = sort_scores[avg_index-1]

        if (front_avg - avg) > (avg - back_avg): # 평균 뒤에 값이 평균에 더 가까울 경우
            print(avg, (scores.index(back_avg)) + 1)

        else: # 평균 앞 뒤 값의 차이가 똑같거나 앞 값이 더 평균에 가까울 경우
            print(avg, (scores.index(front_avg))+1)

def answer():
    n = int(input())
    a = list(map(int, input().split()))
    avg = round(sum(a)/n)
    min = 2147000000
    for index, x in enumerate(a):
        tmp = abs(x - avg) # 절댓값 함수로 거리를 구함
        if tmp < min: # 평균과 더 가까운 값이 나오면
                min = tmp
                score = x
                res = index + 1

        elif tmp == min: # 평균과 같은 차이를 가진 값이 나오면
            if x > score: # 값이 더 큰 값을 찾음
                score = x
                res = index + 1
    print(avg, res)

# 후기
'''
잘못 푼 점
1. sum()을 안썼다.
2. 거리값의 차이로 풀지 않았다. (평균 넣어서 점수들 정렬시키고 앞 뒤 비교함..)

새로 배운 것
1. round 반올림
2. abs 절댓값
'''

