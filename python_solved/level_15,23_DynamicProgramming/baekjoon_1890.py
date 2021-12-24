##### 점프 #####
from sys import stdin
input = stdin.readline
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1
for i in range(N):
  for j in range(N):
    if i == j == 0: continue
    cnt = 0
    for x in range(i - 1, i - 9, -1):
      if x < 0: break
      if arr[x][j] + x == i: cnt += dp[x][j]
    for y in range(j - 1, j - 9, -1):
      if y < 0: break
      if arr[i][y] + y == j: cnt += dp[i][y]
    dp[i][j] = cnt
print(dp[-1][-1])