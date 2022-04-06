# 10진수 N이 입력되면 2진수로 변환하여 출력하는 프로그램을 작성하세요. 
# 단 재귀함수를 이용 해서 출력해야 합니다.
import sys
def DFS(n):
    if n == 0:
        return
    else:
        DFS(n//2)
        print(n%2,end='') # 거꾸로 출력

if __name__=="__main__":
    n = int(input())
    DFS(n)