import sys
sys.setrecursionlimit(10**8) #최대 재귀 깊이를 설정

N = int(sys.stdin.readline())
tree = [[] for _ in range(N+1)] #리스트 안에 리스트
parents = [-1 for _ in range(N+1)] #모두 -1로 초기화 된 부모 리스트
parents[1] = 1
for _ in range(N-1):
    node1, node2 = map(int, sys.stdin.readline().split()) #이어진 두개의 정점 입력 받음
    tree[node1].append(node2)
    tree[node2].append(node1)


def DFS(start, tree, parents):
    for i in tree[start]:
        if parents[i] == -1: #부모노드가 비어있다면
            parents[i] = start
            DFS(i,tree,parents)

DFS(1,tree,parents) #노드1부터 부모노드 체크

for i in range(2, N+1):
    print(parents[i])




    
