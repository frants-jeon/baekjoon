##### 벽 부수고 이동하기 #####
from sys import stdin
from collections import deque
input = stdin.readline

def bfs(start):
  que = deque([start])
  # 3차원 배열 만들어서 visited[0][][]은 벽을 깨지 않은 상태, visited[1][][]은 벽을 깬적이 있는 상태 
  visited = [[[0] * M for _ in range(N)] for _ in range(2)]
  dr = [0, 0, 1, -1]
  dc = [1, -1, 0, 0]
  cnt = 0
  while que:
    cnt += 1
    for _ in range(len(que)):
      w, r, c = que.popleft()
      if not visited[w][r][c]:
        visited[w][r][c] = cnt
        # 도착지까지 왔으면 return
        if r == N - 1 and c == M - 1:
          return cnt
        for i in range(4):
          nr = r + dr[i]
          nc = c + dc[i]
          if 0 <= nr < N and 0 <= nc < M: # 인덱스 범위 안에 포함되고
            # 벽을 만났는데 아직 벽을 깬 적이 없고 벽을 깬 상태의 nr,nc를 방문한 적이 없으면 que에 추가
            if arr[nr][nc] == 1 and w == 0 and not visited[1][nr][nc]:
              que.append([1, nr, nc])
            # 벽이 아니고 방문한 적이 없으면 que에 추가
            elif arr[nr][nc] == 0 and not visited[w][nr][nc]:
              que.append([w, nr, nc])
  return -1

N, M = map(int,input().split())
arr = [list(map(int,input().strip())) for _ in range(N)]
answer = bfs([0,0,0])
print(answer)