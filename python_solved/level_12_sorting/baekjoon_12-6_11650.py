##### 좌표 정렬하기 #####
N = int(input())
li = []
for _ in range(N):
    li.append(tuple(map(int,input().split())))
li.sort()

for pos in li:
    print(pos[0], pos[1])
