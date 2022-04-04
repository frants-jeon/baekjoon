##### 무한 수열 #####
# https://www.acmicpc.net/problem/1351

dp = {0: 1}
def memoization(n):
  if n in dp:
    return dp[n]
  dp[n] = memoization(n // P) + memoization(n // Q)
  return dp[n]


N, P, Q = map(int,input().split())
if N == 0:
  print(1)
else:
  print(memoization(N))
