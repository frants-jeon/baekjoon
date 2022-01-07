##### K번째 수 #####
N, k = int(input()), int(input())
low, high = 0, min(pow(10, 9), pow(N, 2))

def get_cnt(num):
  cnt = 0
  for row in range(1, N + 1):
    cnt += min(num // row, N)
  return cnt

while low + 1 < high:
  mid = (low + high) // 2
  if get_cnt(mid) >= k: high = mid
  else: low = mid
print(high)
