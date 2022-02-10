##### 나이트의 이동 #####
from sys import stdin
from collections import deque
input = stdin.readline

for tc in range(int(input())):
  l = int(input())
  startPos = list(map(int,input().split()))
  goal_r, goal_c = list(map(int,input().split()))
  visited = [[0] * l for _ in range(l)]

  # bfs 시작
  que = deque([startPos])
  dr = [-2, -1, 1, 2, 2, 1, -1, -2]
  dc = [1, 2, 2, 1, -1, -2, -2, -1]
  cnt = 1
  if startPos == [goal_r, goal_c]:
    print(0)
    continue
  
  while que and not visited[goal_r][goal_c]:
    for _ in range(len(que)):
      r, c = que.popleft()
      if not visited[r][c]:
        visited[r][c] = cnt
        for i in range(8):
          nr = r + dr[i]
          nc = c + dc[i]
          if 0 <= nr < l and 0 <= nc < l and not visited[nr][nc]:
            que.append([nr, nc])
    cnt += 1
  print(visited[goal_r][goal_c] - 1)