##### 오르막 수 #####
from sys import stdin
N = int(stdin.readline())
dp = [0 for _ in range(N + 1)]
dp[1] = 10
zero_to_nine = [1 for _ in range(10)]
z_to_n_tmp = [0 for _ in range(10)]
for i in range(2, N + 1):
  z_to_n_tmp[0] = dp[i - 1]
  for j in range(1, 10):
    z_to_n_tmp[j] = z_to_n_tmp[j - 1] - zero_to_nine[j - 1]
  zero_to_nine = z_to_n_tmp
  z_to_n_tmp = [0 for _ in range(10)]
  dp[i] = sum(zero_to_nine) % 10007
print(dp[N]) 