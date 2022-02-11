##### 불 #####
from sys import stdin
from collections import deque
input = stdin.readline

def bfs(fire_s, man_s):
  f_que = deque(fire_s)
  m_que = deque([man_s])
  dw = [1, -1, 0, 0]
  dh = [0, 0, 1, -1]
  cnt = 1
  answer = 0

  # 사람이 이동할 수 없을 때까지 bfs 진행
  while m_que:
    # 불을 먼저 이동
    for _ in range(len(f_que)):
      f_node = f_que.popleft()
      # 방문한 적이 없으면 방문 처리 후 계속 진행
      if visited[f_node[0]][f_node[1]] != -1:
        visited[f_node[0]][f_node[1]] = -1
        # 상하좌우 확인해서 이동 가능하면 que에 추가
        for i in range(4):
          fh = f_node[0] + dh[i]
          fw = f_node[1] + dw[i]
          if fw >= 0 and fw < w and fh >= 0 and fh < h and visited[fh][fw] != -1:
            f_que.append([fh, fw])
            
    # 불의 이동이 끝난 후 사람 이동
    for _ in range(len(m_que)):
      m_node = m_que.popleft()
      # 방문한 적이 없으면 방문 처리 후 계속 진행
      if not visited[m_node[0]][m_node[1]]:
        visited[m_node[0]][m_node[1]] = cnt
        # 답을 구한 적이 없고 탈출 조건이 맞으면 answer 갱신
        if answer == 0:
          if ((m_node[0] != 0 or m_node[0] != h - 1) and (m_node[1] == 0 or m_node[1] == w - 1))\
          or (m_node[0] == 0 or m_node[0] == h - 1):
            answer = cnt

        # 상하좌우 확인해서 이동 가능하면 que에 추가
        for i in range(4):
          mh = m_node[0] + dh[i]
          mw = m_node[1] + dw[i]
          if mw >= 0 and mw < w and mh >= 0 and mh < h and visited[mh][mw] != -1:
            m_que.append([mh, mw])
    cnt += 1
  return answer

for tc in range(int(input())):
  w, h = map(int,input().split())
  visited = [[0] * w for _ in range(h)]
  fire = []
  man = 0

  # 배열 받아서 벽 위치는 이동불가(-1) 표시하고 나머지는 좌표 갱신
  for i in range(h):
    line = list(input().strip())
    for j in range(w):
      if line[j] == '#':
        visited[i][j] = -1
      elif line[j] == '*':
        fire.append([i,j])
      elif man == 0:
        if line[j] == '@':
          man = [i, j]
  
  a = bfs(fire, man)
  print(a if a != 0 else 'IMPOSSIBLE')