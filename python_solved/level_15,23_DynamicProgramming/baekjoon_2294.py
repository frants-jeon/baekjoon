##### 동전 2 #####
from sys import stdin

input = stdin.readline
n, k = map(int,input().split())
coins = set()
for _ in range(n):
  coins.add(int(input()))
coins = sorted(list(coins))
dp = [0 for _ in range(k + 1)]

for money in range(1, k + 1):
  tmp = []
  for coin in coins:
    if coin <= money and dp[money - coin] != -1:
      tmp.append(dp[money - coin])
  if not tmp:
    dp[money] = -1
  else:
    dp[money] = min(tmp) + 1
print(dp[k])