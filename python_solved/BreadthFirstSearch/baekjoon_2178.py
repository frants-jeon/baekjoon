##### 미로 탐색 #####
from sys import stdin
from collections import deque
input = stdin.readline

N, M = map(int,input().split())
arr = [list(map(int,input().strip())) for _ in range(N)]
result = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]

def bfs(r, c):
  que = deque([[r, c]])
  # visited[r][c] = 1
  dr = [-1, 0, 1, 0]
  dc = [0, 1, 0, -1]

  # 큐가 비어있을 때까지 반복
  while que:
    # 큐에서 빼서 노드 탐색
    r, c = que.popleft()
    if not visited[r][c]:
      visited[r][c] = 1
      # 상하좌우 움직일 수 있는지 판단해서 1이면 큐에 추가
      for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if nc >= 0 and nr >= 0 and nr < N and nc < M:
          if arr[nr][nc] and not visited[nr][nc]:  
            que.append([nr, nc])
            result[nr][nc] = result[r][c] + 1

bfs(0,0)
print(1 + result[N - 1][M - 1])