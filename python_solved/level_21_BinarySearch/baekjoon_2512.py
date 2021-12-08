##### 예산 #####
from sys import stdin
input = stdin.readline
N = int(input())
arr = list(map(int,input().split()))
budget = int(input())
low, high = 0, 1000000000

while low + 1 < high:
  mid = (low + high) // 2
  total = 0
  for i in range(N):
    if arr[i] > mid:
      total += mid
    else:
      total += arr[i]
  if total > budget:
    high = mid
  else: low = mid
if low > budget: print(max(arr))
else: print(low)