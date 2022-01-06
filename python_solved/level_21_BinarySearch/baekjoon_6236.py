##### 용돈 관리 #####
from sys import stdin
input = stdin.readline
N, M = map(int,input().split())
arr = [int(input()) for _ in range(N)]
low, high = 0, 100000
while low + 1 < high:
  middle = (low + high) // 2
  current_money = middle
  cnt = 1
  sizeDown = 1
  for i in range(N):
    if arr[i] > middle: sizeDown = 0
    if current_money - arr[i] >= 0:
      current_money -= arr[i]
    else:
      current_money = middle - arr[i]
      cnt += 1
  if sizeDown == 0: low = middle
  elif cnt <= M:
    high = middle
  else:
    low = middle
print(high)