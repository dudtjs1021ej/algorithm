# 1부터 9까지의 자연수로 채워진 7*7 격자판이 주어지면 격자판 위에서 가로방향 또는 세로방향으로 
# 길이 5자리 회문수가 몇 개 있는지 구하는 프로그램을 작성하세요. 
# 회문수란 121과 같이 앞에서부터 읽으나 뒤에서부터 읽으나 같은 수를 말합니다.
import sys
def mySolution():
    a = [list(map(int, input().split())) for _ in range(7)]
    count = 0
    
    for i in range(7):
        for j in range(3):
            start1 = start2 = j
            end1 = end2 = j+4
            # 가로 검사
            while True:
                if start1 == end1: # 같은곳 가르키면 = 모두 다 검사했으면 +1
                    count += 1
                    break
                elif a[i][start1] == a[i][end1]:  # 맨끝 맨앞이 같으면 한칸씩 이동
                    start1 += 1
                    end1 -= 1
                else: # 다르면 회문수가 아님
                    break
            # 세로 검사
            while True:
                if start2 == end2:
                        count += 1
                        break
                elif a[start2][i] == a[end2][i]:
                    start2 += 1
                    end2 -= 1
                else:
                    break
    print(count)
    
def answer():
    board = [list(map(int , input().split())) for _ in range(7)]
    count = 0
    for i in range(3):
        for j in range(7):
            tmp = board[j][i:i+5]
            if tmp == tmp[::-1]: # 뒤집어서 같으면 회문
                count += 1
            for k in range(2):
                if board[i+k][j] != board[i+5-k-1][j]:
                    break
            else:
                count += 1
    print(count)

answer()
# 후기
# 너무 복잡하게 풀었다.
# 가로 검사는 슬라이싱을 이용해서 reverse한 값과 같은걸로 비교하면 되고
# 세로 검사는 while문 쓰지 않고 for문으로 2번만 검사하면 된다.     
