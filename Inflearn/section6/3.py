# 부분집합 구하기
import sys
def DFS(v):
    if v==n+1:
        for i in range(1,n+1):
            if ch[i] == 1:
                print(i, end=' ')
        print()
    else:
        ch[v]=1 # 사용한다
        DFS(v+1)
        ch[v]=0 # 사용하지 않는다
        DFS(v+1)

if __name__=="__main__":
    n = int(input())
    ch = [0]*(n+1)
    DFS(1)

# 사용한다, 사용하지 않는다 두갈래로 나눠서 DFS 사용

