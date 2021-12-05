##### 평범한 배낭 #####
from sys import stdin
input = stdin.readline
N, K = map(int,input().split())
W_V = [(0, 0)]
dp = [[0] * (K + 1) for _ in range(N + 1)]
for _ in range(N):
  w, v = map(int,input().split())
  W_V.append((w, v))

for i in range(1, N + 1):
  weight, value = W_V[i][0], W_V[i][1]
  for j in range(1, K + 1):
    if j >= weight:
      dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)
    else: dp[i][j] = dp[i - 1][j]
print(dp[N][K])