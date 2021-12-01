##### 스티커 #####
from sys import stdin
input = stdin.readline
T= int(input())
for _ in range(T):
  n = int(input())
  r1, r2 = list(map(int,input().split())), list(map(int,input().split()))
  dp = [[-1, -1, -1] for _ in range(n)]
  dp[0] = [0, r1[0], r2[0]]
  for i in range(1, n):
    dp[i][0] = max(dp[i - 1])
    dp[i][1] = max(dp[i - 1][0], dp[i - 1][2]) + r1[i]
    dp[i][2] = max(dp[i - 1][0], dp[i - 1][1]) + r2[i]
  print(max(dp[n - 1]))
