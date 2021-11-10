import sys
from collections import deque
# #최단거리 -> BFS
N, M = map(int, input().split())
map = []
for i in range(N):
        map.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# #    상 하 좌 우
dx = [0,0,1,-1]
dy = [-1,1,0,0]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    #큐가 비어있을 때까지 반복
    while queue:
        x, y = queue.popleft() #pop
        for i in range(4): #pop한 좌표의 상하좌우 모두 체크
            nx = x + dx[i]
            ny = y + dy[i]
            
            # if nx < 0 or nx >= N or ny < 0 or ny >= M: #맵 범위를 벗어나면 넘어감
            #     continue
            # if map[nx][ny] == 0: #벽이라면 넘어감
            #     continue
            if map[nx][ny] == 1 and 0 <= nx < N and 0 <= y < M: #범위안에 있고 방문하지 않았다면 queue에 append하고 +1
                map[nx][ny] = map[x][y]+1
                queue.append((nx, ny))

    return map[N-1][M-1] #오른쪽 아래까지의 최단거리 리턴

print(bfs(0,0))
