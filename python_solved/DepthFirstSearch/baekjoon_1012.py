##### 유기농 배추 #####
from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(3000)

def dfs(x,y):
  global arr, cnt
  # 배열에 배추가 있으면 0으로 만들어 주고
  if arr[y][x]:
    arr[y][x] = 0
    # 4 가지 방향 탐색
    if y - 1 >= 0 and arr[y - 1][x]:
      dfs(x, y - 1)
    if y + 1 < N and arr[y + 1][x]:
      dfs(x, y + 1)
    if x - 1 >= 0 and arr[y][x - 1]:
      dfs(x - 1, y)
    if x + 1 < M and arr[y][x + 1]:
      dfs(x + 1, y)

N = int(input())
for _ in range(N):
  M, N, K = map(int,input().split())
  arr = [[0 for _ in range(M)] for _ in range(N)]
  cnt = 0
  for _ in range(K):
    x, y = map(int,input().split())
    arr[y][x] = 1
  for i in range(M):
    for j in range(N):
      if arr[j][i]:
        # 배추가 있는 곳은 연결된 곳까지 다 0으로 만들어주고  cnt += 1
        dfs(i,j)
        cnt += 1
  print(cnt)
