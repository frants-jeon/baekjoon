##### 다리 놓기 #####
from sys import stdin
input = stdin.readline
T = int(input())
for _ in range(T):
  N, M = map(int,input().split())
  dp = [[0] * M for _ in range(N)]
  dp[0] = [x for x in range(1, M + 1)]
  for i in range(1, N):
    for j in range(i, M):
      if i == j: dp[i][j] = 1
      else:
        dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
  print(max(dp[-1]))