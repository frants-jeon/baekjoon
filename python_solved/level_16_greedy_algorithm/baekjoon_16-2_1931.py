##### 회의실 배정 #####
from sys import stdin

N = int(stdin.readline())
time = []
for _ in range(N):
    time.append(tuple(map(int,stdin.readline().split())))
time.sort(key=lambda x: (x[1], x[0]))

cnt = 0
empty_room_time = 0
for start, end in time:
    if start >= empty_room_time:
        empty_room_time = end
        cnt += 1


print(cnt)
