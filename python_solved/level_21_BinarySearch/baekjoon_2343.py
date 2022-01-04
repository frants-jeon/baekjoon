##### 기타 레슨 #####
from sys import stdin
input = stdin.readline
N, M = map(int,input().split())
lecture = list(map(int,input().split()))
lecture_minute_sum = sum(lecture)
low, high = 0, lecture_minute_sum
while low + 1 < high:
  mid = (low + high) // 2
  blueray_cnt = 1
  total = 0
  sizeDown = 1
  for i in range(N):
    if lecture[i] > mid: sizeDown = 0
    elif total + lecture[i] <= mid:
      total += lecture[i]
    else:
      blueray_cnt += 1
      total = lecture[i]
  if sizeDown == 0: low = mid
  elif blueray_cnt <= M: high = mid
  else: low = mid
print(high)

