##### 동전0 #####
from sys import stdin

N, K = map(int,stdin.readline().split())
coins = []
for _ in range(N):
    coins.append(int(stdin.readline()))
coins.sort(reverse=True)
money = K
cnt = 0
while money != 0:
    for coin in coins:
        if coin > K:
            continue
        cnt += money // coin
        money %= coin

print(cnt)