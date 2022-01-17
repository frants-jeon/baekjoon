##### 외계인의 기타 연주 #####
from sys import stdin
input = stdin.readline

N, P = map(int,input().split())
melody = [list(map(int,input().split())) for _ in range(N)]
# 기타줄 6개를 스택으로 저장. 각 스택의 탑은 누르고 있는 마지막 손가락임
stack = [[0] for _ in range(6)]
cnt = 0

for key in melody:
  line, fret = key[0], key[1]
  # 누르고 있는 손가락(stack의 top)이 연주해야할 음보다 크면 pop
  while stack[line - 1][-1] > fret:
    stack[line - 1].pop()
    cnt += 1
  # 연주해야할 음을 짚고 있으면 안움직여도 되므로, 다른 음을 짚고 있을 때 스택에 추가
  if stack[line - 1][-1] != fret:
    stack[line - 1].append(fret)
    cnt += 1
print(cnt)