##### 이친수 #####
from sys import stdin

N = int(stdin.readline())
dp = [[-1, -1] for _ in range(N)]

def f(n, s):
  if dp[n][s] != -1: return dp[n][s]
  if n == 0: return 1
  if s == 0:
    dp[n][s] = f(n - 1, 0) + f(n - 1, 1)
  else: dp[n][s] = f(n - 1, 0)
  
  return dp[n][s]

print(f(N - 1, 1))