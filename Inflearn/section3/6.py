# N*N의 격자판이 주어지면 
# 각 행의 합, 각 열의 합, 두 대각선의 합 중 가 장 큰 합을 출력합니다.
import sys
def mySolution():
    n = int(input())
    nums = [] # 이중리스트로 넣을 숫자들
    sums = [] # 모든 합들의 리스트
    for _ in range(n):
        a = list(map(int, input().split()))
        nums.append(a)
        sums.append(sum(a)) # 행들의 합

    # 열들의 합
    for i in range(0,n): 
        sum1 = 0
        for j in range(0,n):
            sum1 += nums[j][i]
        sums.append(sum1)

    # 대각선들의 합   
    sum1=sum2=0 
    for i in range(0,n):
        sum1 += nums[i][i] 
        sum2 += nums[i][(n-1)-i]
    sums.append(sum1)
    sums.append(sum2)

    print(max(sums))

def answer():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)] # 입력 n번받고 바로 리스트에 넣음
    largest = -2147000000
    for i in range(n):
        sum1=sum2=0
        for j in range(n):
            sum1 += a[j][i] # 열의 합
            sum2 += a[i][j] # 행의 합
            if largest < sum1:
                largest = sum1
            if largest < sum2:
                largest = sum2

    sum1=sum2=0
    # 대각선의 합
    for i in range(5):
        sum1 += a[i][i]
        sum2 = a[i][n-i-1]
    if largest < sum1:
            largest = sum1
    if largest < sum2:
            largest = sum2

    print(largest)

# 후기
# 입력값 여러번 받고 한번에 리스트에 넣을 수 있음 
# a = [list(map(int, input().split())) for _ in range(n)]
# max 내장함수말고 비교하며 가장 큰 값 찾아야함


