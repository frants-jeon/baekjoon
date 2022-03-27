##### 절댓값 힙 #####
# https://www.acmicpc.net/problem/11286
from heapq import heappop, heappush
from sys import stdin
input = stdin.readline

N = int(input())

def use_heapq():
  heap_p, heap_m = [], []
  for _ in range(N):
    x = int(input())
    if x == 0:
      if not heap_p and not heap_m:
        print(0)
      elif not heap_p:
        print(-heappop(heap_m))
      elif not heap_m:
        print(heappop(heap_p))
      elif heap_p[0] < heap_m[0]:
        print(heappop(heap_p))
      else:
        print(-heappop(heap_m))
    elif x > 0:
      heappush(heap_p, x)
    else:
      heappush(heap_m, -x)

def my_PQ():
  heap = [(0, 0)] # idx 1부터 시작. 튜플 (i, j)에서 i는 x의 절댓값, j는 x의 원래 값
  for _ in range(N):
    x = int(input())
    heap_len = len(heap) - 1 # idx 0을 제외한 힙 길이
    if x == 0: # 출력해야 하는 경우
      # 만약 출력할 값이 없다면 0 출력
      if heap_len == 0:
        print(0)
        continue
      # 출력할 값이 있다면 출력하고 제일 마지막 노드를 루트로 교체
      print(heap[1][1])
      heap[1] = heap[-1] # heap.pop()을 바로 할당할 경우, heap_len == 1인 경우에 에러 발생
      heap.pop()
      heap_len -= 1
      i = 1 # x값이 있는 인덱스

      # x의 자식이 있는 경우에 정렬 진행
      while heap_len >= i * 2:
        # 왼쪽 자식밖에 없는 경우
        if heap_len == i * 2:
          left = heap[i * 2]
          # 자식보다 절댓값이 작은 경우 or 절댓값은 같지만 값이 작은 경우 정렬 불필요하여 정렬 중단.
          if heap[i][0] < left[0]: break
          if heap[i][0] == left[0] and heap[i][1] <= left[1]: break
          # 자식이 더 작은 경우에는 자식이랑 값 교체하면 정렬 끝
          heap[i], heap[i * 2] = left, heap[i]
        else: #양쪽 자식이 다 있는 경우
          left = heap[i * 2]
          right = heap[i * 2 + 1]
          # 양쪽 자식보다 절댓값이 작은 경우 or 절댓값은 같지만 값이 작은 경우 정렬 불필요하여 정렬 중단.
          if heap[i][0] < left[0] and heap[i][0] < right[0]: break
          if heap[i][0] == left[0] == right[0]:
            if heap[i][1] <= left[1] and heap[i][1] <= right[1]: break
          # 값이 더 작은 자식이랑 교체해야 함. 교체 후 i는 자식의 idx로 갱신.
          if left[0] < right[0] or (left[0] == right[0] and left[1] <= right[1]):
            heap[i], heap[i * 2] = left, heap[i]
            i *= 2
          else:
            heap[i], heap[i * 2 + 1] = right, heap[i]
            i *= 2
            i += 1
    
    else: # 값을 추가하는 경우
      heap.append((abs(x), x))
      i = heap_len + 1 # x의 idx
      parent_i = i // 2 # 부모의 idx
      # heap은 idx 1부터 시작이기 때문에 부모가 0보다 크고 부모의 값이 더 크면 부모의 값과 x값 교체.
      while parent_i > 0:
        if heap[parent_i][0] < heap[i][0]: break
        elif heap[parent_i][0] == heap[i][0]:
          if heap[parent_i][1] <= heap[i][1]: break
        heap[parent_i], heap[i] = heap[i], heap[parent_i]
        i = parent_i
        parent_i = i // 2

use_heapq()