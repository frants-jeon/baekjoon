##### 상자넣기 #####
from sys import stdin
input = stdin.readline
n = int(input())
box = list(map(int,input().split()))
dp, dp[0] = [0] * n, 1
for i in range(1, n):
  tmp = []
  for j in range(i):
    if box[i] > box[j]:
      tmp.append(dp[j] + 1)
  if not tmp:
    dp[i] = 1
  else: dp[i] = max(tmp)
print(max(dp))