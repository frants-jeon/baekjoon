##### 최소 힙 #####
# https://www.acmicpc.net/problem/1927
from heapq import heappop, heappush
from sys import stdin
input = stdin.readline

N = int(input())

def use_heapq():
  heap = []
  for _ in range(N):
    x = int(input())
    if x == 0:
      if not heap:
        print(0)
        continue
      print(heappop(heap)[1])
    else:
      heappush(heap, (-x, x))

def my_PQ():
  heap = [0] # idx 1부터 시작
  for _ in range(N):
    x = int(input())
    heap_len = len(heap) - 1 # idx 0을 제외한 힙 길이
    if x == 0: # 출력해야 하는 경우
      # 만약 출력할 값이 없다면 0 출력
      if heap_len == 0:
        print(0)
        continue
      # 출력할 값이 있다면 출력하고 제일 마지막 노드를 루트로 교체
      print(heap[1])
      heap[1] = heap[-1] # heap.pop()을 바로 할당할 경우, heap_len == 1인 경우에 에러 발생
      heap.pop()
      heap_len -= 1
      i = 1 # x값이 있는 인덱스

      # x의 자식이 있는 경우에 정렬 진행
      while heap_len >= i * 2:
        # 왼쪽 자식밖에 없는 경우
        if heap_len == i * 2:
          left = heap[i * 2]
          if heap[i] <= left: break # 자식보다 작아서 정렬이 끝났으면 중단
          # 자식이 더 작은 경우에는 자식이랑 값 교체하면 정렬 끝
          heap[i], heap[i * 2] = left, heap[i]
        else: #양쪽 자식이 다 있는 경우
          left = heap[i * 2]
          right = heap[i * 2 + 1]
          if heap[i] <= left and heap[i] <= right: break # 양쪽 자식들보다 값이 더 작아서 정렬 필요 없으면 중단
          # 값이 더 작은 자식이랑 교체해야 함. 교체 후 i는 자식의 idx로 갱신.
          if left <= right:
            heap[i], heap[i * 2] = left, heap[i]
            i *= 2
          else:
            heap[i], heap[i * 2 + 1] = right, heap[i]
            i *= 2
            i += 1
    
    else: # 값을 추가하는 경우
      heap.append(x)
      i = heap_len + 1 # x의 idx
      parent_i = i // 2 # 부모의 idx
      # heap은 idx 1부터 시작이기 때문에 부모가 0보다 크고 부모의 값이 더 크면 부모의 값과 x값 교체.
      while heap[parent_i] > heap[i] and parent_i > 0:
        heap[parent_i], heap[i] = heap[i], heap[parent_i]
        i = parent_i
        parent_i = i // 2

use_heapq()