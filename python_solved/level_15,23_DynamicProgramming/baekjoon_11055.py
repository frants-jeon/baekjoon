##### 가장 큰 증가 부분 수열 #####
from sys import stdin
input = stdin.readline
N = int(input())
A = list(map(int,input().split()))
dp, dp[0] = [0] * N, A[0]
for i in range(1, N):
  tmp = []
  for j in range(i):
    if A[i] > A[j]: tmp.append(dp[j] + A[i])
  if not tmp: dp[i] = A[i]
  else: dp[i] = max(tmp)
print(max(dp))