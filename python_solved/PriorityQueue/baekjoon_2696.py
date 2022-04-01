from heapq import heappop, heappush
from sys import stdin
input = stdin.readline

for tc in range(int(input())):
  M = int(input())
  heap_min = [] # 중앙값보다 큰 수들
  heap_max = [] # 중앙값보다 작은 수들
  mid = None # 중앙값
  answer = []
  print(M // 2 + 1)
  for _ in range((M + 9) // 10): # 10개 단위로 끊어서 입력
    arr = list(map(int,input().split()))
    for num in arr: # 입력받은 숫자를 돌면서
      # 짝수일 때는 중앙값이 없도록 되어있음
      if mid == None: # 이번에 들어오는 수가 홀수번째 수인 경우
        mid = num # 이번 숫자를 중앙값으로 두고
        # 첫 번째 입력 수인 경우 정답 목록에 추가 후 다음 수로 넘어감
        if not heap_max and not heap_min:
          answer.append(mid)
          continue
        # 입력받은 수가 중앙값보다 더 큰 경우에는 큰 수 목록에서 꺼내서 중앙값으로 갱신
        if mid > heap_min[0]:
          heappush(heap_min, mid)
          mid = heappop(heap_min)
        # 반대의 경우에는 중앙값보다 작은 수 목록에서 꺼내서 중앙값으로 갱신
        else:
          heappush(heap_max, -mid)
          mid = -heappop(heap_max)
        # 중앙값 갱신이 끝난 후, 검사한 중앙값이 10개 미만이면 정답 목록에 추가
        if len(answer) < 10:
          answer.append(mid)
        # 정답 목록이 10개면 출력하고 정답 목록 갱신
        else:
          print(*answer)
          answer = [mid]

      # 입력 값이 짝수인 경우에는 입력값과 기존 중앙값을 비교
      # 큰 수는 큰 수 목록으로, 작은 수는 작은 수 목록으로 넣음
      else:
        if mid > num:
          heappush(heap_min, mid)
          heappush(heap_max, -num)
        else:
          heappush(heap_min, num)
          heappush(heap_max, -mid)
        mid = None # 짝수인 경우에는 중앙값 없음
  print(*answer)