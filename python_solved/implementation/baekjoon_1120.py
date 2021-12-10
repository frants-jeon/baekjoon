##### 문자열 #####
from sys import stdin
A, B = stdin.readline().split()
A_len, B_len = len(A), len(B)
lenth_diff = B_len - A_len
cnt = 0
if lenth_diff == 0:
  for i in range(B_len):
    if A[i] != B[i]: cnt += 1

else:
  tmp = [0 for _ in range(lenth_diff + 1)]
  check = 0
  while check <= lenth_diff:
    for i in range(A_len):
      if A[i] != B[check + i]: tmp[check] += 1
    check += 1
  cnt += min(tmp)
print(cnt)