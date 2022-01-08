##### 회전하는 큐 #####

from collections import deque

N, M = map(int,input().split())
pickList = list(map(int,input().split()))

# 1~N까지의 리스트를 덱으로 생성
deq = deque([i for i in range(1, N + 1)])
answer = 0

for pick in pickList:
  # 첫번째 숫자가 pick이면 뽑기
  if deq[0] == pick:
    deq.popleft()
  # 그게 아니면 뽑아야할 숫자(pick)의 인덱스를 찾아서 
  else:
    idx = deq.index(pick)
    # 가까운 쪽으로 회전 후 answer에 더하고 뽑기
    if len(deq) - idx < idx:
      deq.rotate(len(deq) - idx)
      answer += len(deq) - idx
      deq.popleft()
    else:
      deq.rotate(-idx)
      answer += idx
      deq.popleft()
print(answer)