##### 음식물 피하기 #####
from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(11000)

def dfs(x, y):
  global cnt
  # 배열에 음식물이 있으면 0으로 만들어 주고 음식물의 크기를 더해줌
  if arr[x][y]:
    arr[x][y] = 0
    cnt += 1
    # 4 가지 방향 탐색
    if y - 1 >= 0 and arr[x][y - 1]:
      dfs(x, y - 1)
    if y + 1 < M and arr[x][y + 1]:
      dfs(x, y + 1)
    if x - 1 >= 0 and arr[x - 1][y]:
      dfs(x - 1, y)
    if x + 1 < N and arr[x + 1][y]:
      dfs(x + 1, y)

N, M, K = map(int,input().split())
arr = [[0] * M for _ in range(N)]
cnt = 0
bigest = 0
for _ in range(K):
  x, y = map(int,input().split())
  # 음식물이 있으면 True로 바꿔주기
  arr[x - 1][y - 1] = 1

for i in range(N):
  for j in range(M):
    if arr[i][j]:
      dfs(i,j)
      bigest = max(bigest, cnt)
      cnt = 0
print(bigest)