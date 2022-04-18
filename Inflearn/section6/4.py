# 합을 두 개의 부분집합으로 나누었을 때 
# 두 부분집합의 원소의 합이 서로 같은 경우가 존재하면 “YES"를 출력하고, 
# 그렇지 않으면 ”NO"를 출력하는 프로그램을 작성하세요.
import sys

def DFS(L, sum): # 인덱스, 부분집합 원소 합 누적
    if sum>total//2: # 총 합을 넘어서면 절대 같을수가 없기떄문에 바로 NO
        return
    if L==n:
        if sum == (total-sum):
            print("YES")
            sys.exit(0)
    else:
        DFS(L+1,sum+a[L])
        DFS(L+1,sum)
    

if __name__=="__main__":
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    DFS(0,0)
    print("NO")


# 사용한다, 사용하지 않는다로 나누고 sum을 매개변수로 같이 가지고 가며 풀이
