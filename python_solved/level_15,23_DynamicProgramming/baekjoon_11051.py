##### 이항 계수 2 #####
from sys import stdin, setrecursionlimit
setrecursionlimit(2000)
N, K = map(int,stdin.readline().split())
dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
def b_c(n, k):
  if n == 0 or n == k or k == 0:
    dp[n][k] = 1
    return 1
  if dp[n][k] != 0: return dp[n][k]
  dp[n][k] = (b_c(n - 1, k - 1) + b_c(n - 1, k)) % 10007
  return dp[n][k]
print(b_c(N, K))