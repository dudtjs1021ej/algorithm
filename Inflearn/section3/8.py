# 격자의 행을 기준으로 왼쪽, 또는 오른쪽으로 회전시켜 위치를 변경해 모든 감이 잘 마르게 합니다.
# 만약 회전명령 정보가 2 0 3이면 2번째 행을 왼쪽으로 3만큼 아래 그림처럼 회전시키는 명령 입니다.
# 첫 번째 수는 행번호, 두 번째 수는 방향인데 0이면 왼쪽, 1이면 오른쪽이고, 세 번째 수는 회 전하는 격자의 수입니다.
# M개의 회전명령을 실행하고 난 후 아래와 같이 마당의 모래시계 모양의 영역에는 감 이 총 몇 개가 있는지 출력하는 프로그램을 작성하세요.
import sys
def mySolution():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]

    m = int(input())
    b = [list(map(int, input().split())) for _ in range(m)]

    for i in range(m):
        row = b[i][0] - 1 # 행번호(0부터 시작)
        direction = b[i][1] # 방향
        num = b[i][2] # 회전수
        
        if direction == 0: # 왼쪽으로 회전
            for _ in range(num):
                a[row].append(a[row].pop(0)) # 맨앞빼서 맨뒤에 붙임
        else: # 오른쪽으로 회전
            for _ in range(num):
                a[row].insert(0, a[row].pop()) # 맨뒤빼서 맨앞에 붙임

    sum = 0
    left = 0
    right = n-1
    for i in range(n):
        print(i,left,right)
        for j in range(left, right+1):
            sum += a[i][j]
        if i < n//2:
            left += 1
            right -= 1
        else:
            left -= 1
            right += 1

    print(sum)

def answer():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]

    m = int(input())

    for _ in range(m):
        row, direction, num = map(int, input().split())
        if direction == 0: # 왼쪽으로 회전
            for _ in range(num):
                a[row-1].append(a[row-1].pop(0)) # 맨앞빼서 맨뒤에 붙임
        else: # 오른쪽으로 회전
            for _ in range(num):
                a[row-1].insert(0, a[row-1].pop()) # 맨뒤빼서 맨앞에 붙임

    sum = 0
    left = 0
    right = n-1
    for i in range(n):
        print(i,left,right)
        for j in range(left, right+1):
            sum += a[i][j]
        if i < n//2:
            left += 1
            right -= 1
        else:
            left -= 1
            right += 1

    print(sum)

# 후기
# m을 이중리스트로 받을필요없이 row, direction, num 세개 바로 input으로 받아서 풀면 됨 (이 부분 제외 같게 품)

