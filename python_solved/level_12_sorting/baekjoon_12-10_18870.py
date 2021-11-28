##### 좌표 압축 #####
from sys import stdin
N = int(stdin.readline())
x = enumerate(list(map(int,stdin.readline().split())))
pos = []
for i in x:
    pos.append(list(i))
cmprs_pos = {}



pos.sort(key=lambda x: x[1])
answer_num = 0
answer_pos = {0: 0}
for i in range(1, N):
    if pos[i][1] != pos[i - 1][1]:
        answer_num += 1
    answer_pos[i] = answer_num

for j in range(N):
    pos[j][1] = answer_pos[j]

pos.sort(key= lambda x: x[0])
for k in range(N):
    print(pos[k][1], end=' ')

