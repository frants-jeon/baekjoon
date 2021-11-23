import sys

N = int(input())
li = []
for _ in range(N):
    x, y = map(int,sys.stdin.readline().split())
    num = (y, x)
    li.append(num)
li.sort()

for pos in li:
    print(pos[1], pos[0])
