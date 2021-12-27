##### 퇴사 #####
from sys import stdin
input = stdin.readline
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)] # arr[i][0]이 시간(T), arr[i][1]이 금액(P)
dp = [0] * (N + 1)
for i in range(N - 1, -1, -1):
  if arr[i][0] + i > N:
    dp[i] = dp[i + 1]
  else: dp[i] = max(dp[i + 1], arr[i][1] + dp[i + arr[i][0]])
print(dp[0])