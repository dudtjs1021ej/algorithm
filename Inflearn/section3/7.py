# 현수의 농장은 N*N 격자판으로 이루어져 있으며, 각 격자안에는 한 그루의 사과나무가 심어저 있다.
#  N의 크기는 항상 홀수이다. 
# 가을이 되어 사과를 수확해야 하는데 현수는 격자판안의 사과를 수확할 때
#  다이아몬드 모양의 격자판만 수확하고 나머지 격자안의 사과는 새들을 위해서 남겨놓는다.
# 현수과 수확하는 사과의 총 개수를 출력하세요.
import sys
def mySolution():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    mid = n//2
    left = right = mid# left,right 가운데에서 시작
    sum1 = 0
    for i in range(n):
        if i < mid:
            sum1 += sum(a[i][left:right+1])
            left -= 1
            right += 1

        elif i == mid:
            sum1 += sum(a[i][:])
            left += 1
            right -= 1

        else:
            sum1 += sum(a[i][left:right+1])
            left += 1
            right -= 1
    print(sum1)

def answer():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    res = 0
    s=e=n//2
    for i in range(n):
        for j in range(s,e+1):
            res += a[i][j]
        if i < n//2:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1

# 후기
# start, end 두개의 포인터를 넣어 계산하는 방식은 거의 유사하게 풀었음
# 다르게 푼 점 - 리스트안의 값 합을 슬라이싱과 sum 내장함수로 풀었지만 for문 두번 돌아서 더하는걸로 풀어야함 (내장함수 최대한 쓰지말자)


