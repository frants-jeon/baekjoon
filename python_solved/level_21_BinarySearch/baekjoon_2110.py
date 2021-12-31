##### 공유기 설치 #####
from sys import stdin
input = stdin.readline
N, C = map(int,input().split())
arr = sorted([int(input()) for _ in range(N)])
low, high = 0, 1000000000
while low + 1 < high:
  middle = (low + high) // 2
  current_house = arr[0]
  cnt = 1
  for i in range(1, N):
    if arr[i] - current_house >= middle:
      current_house = arr[i]
      cnt += 1
  if cnt < C: high = middle
  else: low = middle
print(low)