##### 수 정렬하기 2 #####
import sys

N = int(input())
l = []
for _ in range(N):
    l.append(int(sys.stdin.readline()))

l.sort()

for num in l:
    print(num)
