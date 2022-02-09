##### 상범 빌딩 #####
from sys import stdin
from collections import deque
input = stdin.readline

def bfs(start):
  que = deque([start])
  # 3차원 배열 상하동서남북 이동
  dl = [1, -1, 0, 0, 0, 0]
  dr = [0, 0, 0, 0, 1, -1]
  dc = [0, 0, 1, -1, 0, 0]

  while que:
    l, r, c = que.popleft()
    # 큐에서 좌표 꺼냄. 해당 좌표를 방문한 적이 없으면 방문처리
    if not visited[l][r][c]:
      visited[l][r][c] = 1
      # 상하동서남북 방향 돌면서 이동 가능하면 큐에 추가하고 결과 저장
      for i in range(6):
        nl = l + dl[i]
        nr = r + dr[i]
        nc = c + dc[i]
        if nl >= 0 and nl < L \
          and nr >= 0 and nr < R \
          and nc >= 0 and nc < C:
          if building[nl][nr][nc] != '#':
            que.append([nl, nr, nc])
            result[nl][nr][nc] = result[l][r][c] + 1


while 1:
  L, R, C = map(int,input().split())
  if L == R == C == 0: break
  building = []
  S_pos, E_pos = 0, 0
  # 3차원 배열 받으면서 S와 E 좌표 갱신
  for i in range(L):
    floor = []
    for j in range(R):
      r = list(input().strip())
      if S_pos == 0:
        if 'S' in r:
          S_pos = [i,j,r.index('S')]
      if E_pos == 0:
        if 'E' in r:
          E_pos = [i,j,r.index('E')]
      floor.append(r)
    input()
    building.append(floor)
  
  visited = [[[0] * C for _ in range(R)] for _ in range(L)]
  result = [[[0] * C for _ in range(R)] for _ in range(L)]
  bfs(S_pos)
  ans = result[E_pos[0]][E_pos[1]][E_pos[2]]
  print(f'Escaped in {ans} minute(s).' if ans != 0 else 'Trapped!')
