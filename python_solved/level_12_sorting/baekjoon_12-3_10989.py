##### 수 정렬하기 3 #####
import sys

N = int(input())
li = [0] * 10000
for _ in range(N):
    li[(int(sys.stdin.readline())) - 1] += 1


for i in range(10000):
    cnt = li[i]
    if cnt != 0:
        for _ in range(cnt):
            print(i + 1)