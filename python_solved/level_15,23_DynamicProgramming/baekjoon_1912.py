##### 연속합 #####
from sys import setrecursionlimit
setrecursionlimit(200000)

def memoization(n, arr):
  if n < 0: return 0
  if dp[n] != 0: return dp[n]
  dp[n] = max(memoization(n - 1, arr) + arr[n], arr[n])
  return dp[n]

n = int(input())
arr = list(map(int,input().split()))
dp = [0] * n
memoization(n - 1, arr)
print(max(dp))