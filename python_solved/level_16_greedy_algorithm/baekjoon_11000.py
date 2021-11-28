##### 강의실 배정 #####s
from sys import stdin
from queue import PriorityQueue
N = int(stdin.readline())
using_room = PriorityQueue(maxsize= 200000)
lesson_time = []

for _ in range(N):
    start, end = map(int,stdin.readline().split())
    lesson_time.append((end, start))
lesson_time.sort(key=lambda x: (x[1], x[0]))
using_room.put(lesson_time[0])
answer = 0
for i in range(1, N):
    lesson = using_room.get()
    lesson_now = lesson_time[i]
    while lesson[0] <= lesson_now[1] and not using_room.empty():
        lesson = using_room.get()
    if lesson[0] > lesson_now[1]:
        using_room.put(lesson)
    using_room.put(lesson_now)
    answer = max(answer,using_room.qsize())
    
print(answer)
