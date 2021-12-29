##### 게임 개발 #####
from sys import stdin
input = stdin.readline
N = int(input())
arr = [0] + [list(map(int,input().split())) for _ in range(N)]
dp = [0] * (N + 1)
def build(n):
  if dp[n] != 0: return dp[n]
  needs = arr[n][1:-1]
  if not needs:
    dp[n] = arr[n][0]
    return dp[n]
  else:
    tmp = []
    for need in needs:
      if dp[need] == 0:
        tmp.append(build(need) + arr[n][0])
      else: tmp.append(dp[need] + arr[n][0])
    dp[n] = max(tmp)
    return dp[n]

for j in range(1, N + 1):
  print(build(j))