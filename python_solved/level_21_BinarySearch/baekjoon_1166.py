##### 선물 #####
size = list(map(int,input().split()))
N = size.pop(0)
low, high = 0, min(size) * 2
for _ in range(100):
  mid = (low + high) / 2
  x, y, z = size[0] // mid, size[1] // mid, size[2] // mid
  cnt = x * y * z
  if int(cnt) >= N:
    low = mid
  else: high = mid
print(low)