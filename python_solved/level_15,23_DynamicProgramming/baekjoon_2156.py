##### 포도주 시식 #####
from sys import stdin
input = stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]
# dp[i][0] = arr[i] + arr[i-1] 선택 / dp[i][1] = arr[i] + arr[i-2]선택 / dp[i][2] = arr[i-1] + arr[i-2] 선택
dp = [[0,0,0] for _ in range(n)]
if n == 1: print(arr[0])
else:
  dp[0], dp[1] = [arr[0], arr[0], 0], [sum(arr[:2]), arr[1], arr[0]]
  for i in range(2, n):
    dp[i][0] = arr[i] + dp[i - 1][1]
    dp[i][1] = arr[i] + dp[i - 1][2]
    dp[i][2] = max(dp[i - 1])
  print(max(dp[-1]))