# 완성된 9×9 크기의 수도쿠가 주어지면 정확하게 풀었으면 “YES", 
# 잘 못 풀었으면 ”NO"를 출력하는 프로그램을 작성하세요.
import sys

def mySolution():
    def check_sudoku(a):     
        for i in range(9):
            ch1 = [0]*10 # 행 체크
            ch2 = [0]*10 # 열 체크
            for j in range(9):
                ch1[a[i][j]] = 1
                ch2[a[j][i]] = 1
            if sum(ch1) != 9 or sum(ch2) != 9:
                return False
            
        # 3*3 체크 -> 잘못 품 (0~3 행만 체크)
        # for i in range(0,9,3):
        #     ch3 = [0]*10
        #     for j in range(i,i+3):
        #         for k in range(i,i+3):
        #             ch3[a[j][k]] = 1
        #     if sum(ch3) != 9:
        #         return False
       
        for i in range(3):
            for j in range(3):
                ch3 = [0]*10
                for k in range(3):
                    for s in range(3):
                        ch3[a[i*3 + k][j*3 + s]] = 1
                if sum(ch3) != 9:
                    return False
        return True
        
    a = [list(map(int , input().split())) for _ in range(9)]
    if check_sudoku(a):
        print("YES")
    else:
        print("NO")

mySolution()

# 후기
# 잘못 푼 점
# 1 .집합으로 바꾸고 리스트와 길이가 다르면 False 리턴으로 풀이했음
# 2. 3*3 체크할 때, 위에 0~3 행만 체크했음

# 새로 배운 것
# 중복 체크 : 새로운 리스트 만들고 해당 숫자있으면 그 숫자를 인덱스로 보고 1로 만들어 sum으로 확인