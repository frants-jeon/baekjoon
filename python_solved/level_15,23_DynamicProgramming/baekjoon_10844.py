##### 쉬운 계단 수 #####
from sys import stdin
N = int(stdin.readline())
dp, dp[0], dp[0][0] = [[0] * 10 for _ in range(N)], [1] * 10, 0
for i in range(1, N):
  for j in range(10):
    if j == 0:
      dp[i][j] = dp[i - 1][1]
    elif j == 9:
      dp[i][j] = dp[i - 1][8]
    else:
      dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
print(sum(dp[-1]) % 1000000000)