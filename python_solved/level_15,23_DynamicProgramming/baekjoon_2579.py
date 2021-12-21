##### 계단 오르기 #####
from sys import stdin
input = stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]
dp = [[0,0] for _ in range(n)]
if n == 1: print(arr[0])
else:
  dp[0], dp[1] = [arr[0],0], [arr[0] + arr[1],arr[1]]
  for i in range(2, n):
    dp[i][0] = dp[i - 1][1] + arr[i]
    dp[i][1] = max(dp[i - 2]) + arr[i]
  print(max(dp[-1]))