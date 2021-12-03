##### 카드 구매하기 #####
from sys import stdin
input = stdin.readline
N = int(input())
P = list(map(int,input().split()))
P.insert(0, 0)
dp = [0 for _ in range(N + 1)]
for i in range(1, N + 1):
  tmp = [P[i]]
  for j in range(1, i):
    tmp.append(dp[i - j] + dp[j])
  dp[i] = max(tmp)
print(dp[N])