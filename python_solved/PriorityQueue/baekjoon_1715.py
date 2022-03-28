##### 카드 정렬하기 #####
# https://www.acmicpc.net/problem/1715
from heapq import heapify, heappop, heappush
from sys import stdin
input = stdin.readline

N = int(input())
heap = [int(input()) for _ in range(N)]
heapify(heap)
ans = 0
for i in range(N - 1):
  tmp = heappop(heap) + heappop(heap)
  heappush(heap, tmp)
  ans += tmp
print(ans)