##### 도토리 숨기기 #####
from sys import stdin
input = stdin.readline
N, K, D = map(int,input().split())
# K개의 규칙을 2차원 배열로 저장
rules = [list(map(int,input().split())) for _ in range(K)]
low, high = 0, N
while low + 1 < high:
  #mid = 앞에 몇개의 도토리가 있는지 확인하고자 하는 상자 번호
  mid = (low + high) // 2 
  # cnt = 도토리 개수
  cnt = 0
  for rule in rules:
    if mid >= rule[0]:
      cnt += (min(mid, rule[1]) - rule[0]) // rule[2] + 1
  # mid 번째 상자까지 들어있는 도토리가 D보다 많거나 같으면 앞쪽 탐색(high = mid)
  if cnt >= D: high = mid
  else: low = mid
print(high)