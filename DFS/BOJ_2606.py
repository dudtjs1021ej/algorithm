import sys
sys.setrecursionlimit(10**8) #최대 재귀 깊이를 설정

N = int(sys.stdin.readline()) 
M = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]
virus = [0 for _ in range(N+1)] #바이러스에 걸렸으면 1 아니면 0
for _ in range(M):
    vertex1, vertex2 = map(int,sys.stdin.readline().split())
    graph[vertex1].append(vertex2)
    graph[vertex2].append(vertex1)

def DFS(start, graph, virus):
    for i in graph[start]:
        if virus[i] == 0: #아직 감염되지 않았다면
                virus[i] = 1
                DFS(i, graph, virus)

virus[1] = 1 #정점1은 감염됨
DFS(1, graph, virus)
count = 0
for i in range(N+1):
    if virus[i] == 1: count += 1

print(count-1) #자신(정점1) 제외하고 출력
