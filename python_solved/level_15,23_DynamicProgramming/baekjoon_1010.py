##### 다리 놓기 #####
from sys import stdin
input = stdin.readline

def bottom_up():
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


def top_down():
  for tc in range(int(input())):
    N, M = map(int,input().split())
    # dp[n][m] = 서쪽에 다리가n개, 동쪽에 다리가 m개일 때 지을 수 있는 다리 갯수
    dp = [[0] * M for _ in range(N)]
    def memoization(n, m):
      if dp[n][m] != 0: 
        return dp[n][m]
      if n == m:
        dp[n][m] = 1
        return dp[n][m]
      if n == 0:
        dp[n][m] = m + 1
        return dp[n][m]
      dp[n][m] = memoization(n - 1, m - 1) + memoization(n, m - 1)
      return dp[n][m]
    memoization(N - 1, M - 1)
    print(max(dp[-1]))
