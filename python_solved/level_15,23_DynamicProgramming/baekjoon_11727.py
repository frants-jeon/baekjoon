##### 2xn 타일링 2 #####
from sys import stdin
n = int(stdin.readline())
dp = [-1 for _ in range(n + 1)]
dp[0], dp[1] = 1, 3

for i in range(2, n + 1):
  dp[i] = (2 * dp[i - 2] + dp[i - 1]) % 10007

print(dp[n - 1])