##### 가장 긴 증가하는 부분 수열 #####
from sys import stdin
input = stdin.readline
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