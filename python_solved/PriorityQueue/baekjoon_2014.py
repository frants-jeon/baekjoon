##### 소수의 곱 #####
# https://www.acmicpc.net/problem/2014
from heapq import heappop, heappush

K, N = map(int,input().split())
prime_nums = list(map(int,input().split()))
heap = []
bigest = pow(2, 31) # 답이 될 수 있는 최댓값
# 기존 주어진 소수들을 힙에 넣고 시작
for prime in prime_nums:
  heappush(heap, prime)

cnt = 0 # pop횟수
last_num = 0 # pop했던 숫자
# N번 뽑을 때까지 pop진행
while cnt < N:
  cur = heappop(heap)
  # 마지막 뽑은 숫자와 중복이 아닌 경우에만 카운팅
  if last_num != cur:
    last_num = cur
    cnt += 1
    # 뽑은 숫자에 소수들을 각각 곱해서 heappush
    for prime in prime_nums:
      if cur * prime > bigest: break # 최댓값을 넘어가면 중단
      heappush(heap, cur * prime)

print(last_num)