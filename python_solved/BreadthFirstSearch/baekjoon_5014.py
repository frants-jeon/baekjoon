##### 스타트링크 #####
from collections import deque

F, S, G, U, D = map(int,input().split())
visited = [-1] + [0] * F
visited[S] ,visited[G] = 'S', 'G'

def bfs(F, start, G, up, down):
  que = deque()
  # bfs를 시작하기 위해 append
  if start + up <= F:
    que.append(start + up)
  if start - down > 0:
    que.append(start - down)
  btn_cnt = 0
  
  while que:
    # 버튼을 한 번 누르면 갈 수 있는 곳 bfs 시작
    btn_cnt += 1
    for _ in range(len(que)):
      cf = que.popleft()
      if not visited[cf] or visited[cf] == 'G':
        visited[cf] = btn_cnt
        uf, df = cf + up, cf - down
        if uf <= F:
          if not visited[uf] or visited[uf] == 'G':
            que.append(uf)
        if df > 0:
          if not visited[df] or visited[df] == 'G':
            que.append(df)
    if visited[G] != 'G': break # 목표지점에 도달했으면 중단

  # visited[G]가 그대로 G이면 도달하지 못했다는 것이므로 -1로 return
  if visited[G] == 'G':
    btn_cnt = -1
  return btn_cnt

# 이미 도착지점에 있으면 0으로 해주고 아니면 bfs시작
if S == G:
  answer = 0
else:
  answer = bfs(F, S, G, U, D)

print(answer if answer != -1 else 'use the stairs') # 양식대로 출력