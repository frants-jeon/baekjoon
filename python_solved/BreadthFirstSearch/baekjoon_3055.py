##### 탈출 #####
from collections import deque

R, C = map(int,input().split())
hedgehog = 0 # 두더지 좌표
water = [] # 물이 있는 좌표
goal_r, goal_c = [0, 0] # 목표지점 좌표
visited = [[0] * C for _ in range(R)]
for i in range(R):
  line = list(input())
  # visited 배열에 돌이 있는 곳 = -1, 목표지점 = 'D' 표시
  for j in range(C):
    if line[j] == '*':
      water.append([i, j])
    elif line[j] == 'X':
      visited[i][j] = -1
    elif line[j] == 'D':
      goal_r, goal_c = [i, j]
      visited[i][j] = 'D'
    elif line[j] == 'S':
      hedgehog = [i, j]

def bfs():
  w_que = deque(water)
  h_que = deque([hedgehog])
  dr = [0, 0, 1, -1]
  dc = [1, -1, 0, 0]
  cnt = 0

  while h_que:
    cnt += 1
    for _ in range(len(w_que)):
      wr, wc = w_que.popleft()
      # 이미 갔던 곳이나 돌이 있는 곳이나 목표지점이 아니면 방문 가능
      if visited[wr][wc] != -1 and visited[wr][wc] != 'D':
        visited[wr][wc] = -1
        for i in range(4):
          nr = wr + dr[i]
          nc = wc + dc[i]
          if 0 <= nr < R and 0 <= nc < C:
            if visited[nr][nc] != -1 and visited[nr][nc] != 'D':
              w_que.append([nr, nc])
    
    for _ in range(len(h_que)):
      hr, hc = h_que.popleft()
      # 목표지점이면 표시해주고 bfs 중단
      if visited[hr][hc] == 'D':
        visited[hr][hc] = cnt
        break
      if not visited[hr][hc]:
        visited[hr][hc] = cnt
        for i in range(4):
          nr = hr + dr[i]
          nc = hc + dc[i]
          if 0 <= nr < R and 0 <= nc < C:
            if not visited[nr][nc] or visited[nr][nc] == 'D':
              h_que.append([nr, nc])
    # 목표지점이 'D'가 아니라 숫자면 도착했다는 뜻이므로 bfs 중단
    if visited[goal_r][goal_c] != 'D': break

  if visited[goal_r][goal_c] == 'D':
    cnt = 0
  return cnt - 1

answer = bfs()
print(answer if answer != -1 else 'KAKTUS')