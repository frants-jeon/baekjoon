##### 토마토 #####
from sys import stdin
from collections import deque
input = stdin.readline

M, N = map(int,input().split())
arr = []
tomato = []
visited = [[0] * M for _ in range(N)]
que_arr = [[0] * M for _ in range(N)] # 시간초과 때문에 해당 배열 사용. 자세한건 아래에서 설명.
for i in range(N):
  line = list(map(int,input().split()))
  for j in range(M):
    if line[j] == 1:
      tomato.append([i,j])
      # 큐에 들어가 있는 요소들을 좌표에도 표시
      que_arr[i][j] = 1
    elif line[j] == -1:
      visited[i][j] = -1

# bfs 시작
def bfs(start):
  que = deque(start)
  dr = [0, 0, 1, -1]
  dc = [1, -1, 0, 0]
  cnt = 0
  while que:
    cnt += 1
    for _ in range(len(que)):
      r, c = que.popleft()
      # 큐에서 빠지면 que_arr에도 표시
      que_arr[r][c] = 0
      if not visited[r][c]:
        visited[r][c] = cnt
        for i in range(4):
          nr = r + dr[i]
          nc = c + dc[i]
          if 0 <= nr < N and 0 <= nc < M:
            # 큐에 있는지 중복 체크 안하고 넣으면 모든 배열이 다 체크 됐음에도(모든 토마토가 익었음에도) while문을 돌면서 answer += 1이 됨
            # 그래서 [nr, nc] in que로 체크하면 시간초과 돼서 que_arr배열 생성함.
            if not visited[nr][nc] and not que_arr[nr][nc]:
              que.append([nr, nc])
              que_arr[nr][nc] = 1
  return cnt

# global에서 bfs하는 것보다 함수 호출해서 하는게 1초 정도 더 빠르게 나옴.
answer = bfs(tomato)
for i in range(N):
  if 0 in visited[i]:
    answer = 0
    break

print(answer - 1)

'''
11 11
0 0 0 0 1 0 -1 -1 0 0 0 
0 -1 1 1 0 0 1 1 0 0 0 
0 0 0 0 -1 1 0 0 1 0 0 
0 0 -1 0 0 -1 -1 0 0 0 -1 
1 1 -1 0 0 1 0 0 0 -1 1 
-1 0 0 0 0 0 1 0 0 1 0 
0 1 0 -1 0 0 0 0 1 1 1 
0 0 0 1 0 0 0 0 0 -1 0 
0 0 0 0 0 0 0 0 0 0 -1 
-1 0 0 0 0 0 1 1 0 0 1 
-1 0 0 0 0 -1 -1 0 0 0 -1
answer = 4
'''
