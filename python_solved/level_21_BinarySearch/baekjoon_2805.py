##### 나무 자르기 #####
from sys import stdin
input = stdin.readline
N, M = map(int,input().split())
arr = list(map(int,input().split()))
low, high = 0, 1000000000
lenth = len(arr)
while low + 1 < high:
  mid = (low + high) // 2
  total = 0
  for i in range(lenth):
    if arr[i] > mid:
      total += arr[i] - mid
      if total >= M: break
  if total >= M: low = mid
  else: high = mid
print(low)
