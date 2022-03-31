##### N번째 큰 수 #####
# https://www.acmicpc.net/problem/2075
from heapq import heappop, heappush, heapify
from sys import stdin
input = stdin.readline

N = int(input())
# 제일 첫줄을 힙에 넣고 시작
heap = list(map(int,input().split()))
heapify(heap)

for _ in range(N - 1):
  # 그 다음 줄부터 차례대로 힙에 넣고 빼줌
  tmp = list(map(int,input().split()))
  for num in tmp:
    heappush(heap, num)
    heappop(heap)
    
# 마지막 남은 N개의 원소 중에 제일 작은 수(힙의 루트)가 N번째 큰 수
print(heap[0])