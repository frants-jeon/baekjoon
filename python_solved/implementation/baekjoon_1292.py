##### 풀기 쉬운 문제 #####
from sys import stdin
A, B = map(int,stdin.readline().split())
answer = 0
cnt = 1
num = 0
while cnt <= B:
  num += 1
  for _ in range(num):
    if cnt >= A and cnt <= B:
      answer += num
    cnt += 1
print(answer)