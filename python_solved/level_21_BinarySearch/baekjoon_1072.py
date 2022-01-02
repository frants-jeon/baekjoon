##### 게임 #####
from sys import stdin
X, Y = map(int,stdin.readline().split())
Z = int(100 * Y / X)
low, high = 0, 1000000001
while low + 1 < high:
  middle = (low + high) // 2
  if int(100 * (Y + middle) / (X + middle)) == Z:
    low = middle
  else: high = middle
if high == 1000000001: print(-1)
else: print(high)