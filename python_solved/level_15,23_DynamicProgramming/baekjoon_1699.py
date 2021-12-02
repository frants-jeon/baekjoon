##### 제곱수의 합 #####
from sys import stdin

N = int(stdin.readline())
dp = [-1 for _ in range(N + 1)]
dp[:2] = 'x', 1
all_sq_list = [pow(x, 2) for x in range(1, 318)]
for i in range(2, N + 1):
  sq_list = []
  if dp[i] == -1:
    for k in all_sq_list:
      if k > i: break
      if k == i:
        sq_list.append(1)
      else:
        sq_list.append(dp[k] + dp[i - k])
    dp[i] = min(sq_list)
print(dp[N])
