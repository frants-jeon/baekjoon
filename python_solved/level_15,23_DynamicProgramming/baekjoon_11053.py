##### 가장 긴 증가하는 부분 수열 #####
from sys import stdin
input = stdin.readline

def bottom_up():
  N = int(input())
  arr = list(map(int,input().split()))
  dp, dp[0] = [0] * N, 1
  for i in range(1, N):
    tmp = []
    for j in range(i):
      if arr[j] < arr[i]:
        tmp.append(dp[j] + 1)
    if not tmp: dp[i] = 1
    else: dp[i] = max(tmp)
  print(max(dp))


def top_down():
  N = int(input())
  arr = list(map(int,input().split()))
  dp = [0] * N
  def memoization(n):
    if dp[n] != 0: return dp[n]
    if n == 0:
      dp[n] = 1
      return 1
    tmp = []
    for i in range(n - 1, -1, -1):
      if arr[i] < arr[n]:
        tmp.append(memoization(i))
    if tmp:
      dp[n] = max(tmp) + 1
    else: dp[n] = 1
    return dp[n]
  # dp값 안구하고 건너뛰는 경우도 있어서 반복문으로 다 구해줌.
  for i in range(N - 1, -1, -1):
    if dp[i] == 0:
      memoization(i)
  print(max(dp))
