##### 퍼즐 #####
from collections import deque

def bfs(start, zero):
  que = deque([[start, zero]])
  # dict형태로 방문 여부 체크와 큐에 이미 있는지 여부 체크
  visited = dict()
  is_in_que = {list_to_str(start): 0}
  move = [-3, 1, 3, -1]
  cnt = -1 # 교환 횟수(최초 상태도 큐를 돌며 +1이 되기 때문에 -1부터 시작)
  while que:
    cnt += 1
    for _ in range(len(que)):
      current_arr, zero_idx = que.popleft()
      is_in_que.pop(current_arr) # 큐에서 빠지면 큐 중복 확인dict도 같이 제거
      # 정답을 만들 수 있으면 교환 횟수 리턴
      if current_arr == '123456789':
        return cnt
      # 방문한 적이 없으면 방문 추가 해주고 탐색 진행
      if visited.get(current_arr, -1) == -1:
        visited[current_arr] = cnt
        for i in range(4):
          # 3씩 이동하는 것은 행이동, 1씩 이동하는 것은 열이동으로 나눠서 조건 확인하여 이동 가능 여부 체크.
          if (abs(move[i]) == 3 and 0 <= zero_idx + move[i] < 9)or\
             (abs(move[i]) == 1 and 0 <= zero_idx % 3 + move[i] < 3):
            # 이동 가능하면 이동(교환) 진행
            n_arr = change(current_arr, zero_idx, zero_idx + move[i])
            n_zero_idx = zero_idx + move[i]
            # 이동한 진행한 배열을 방문한 적이 없고 큐에 없으면 큐에 추가
            if visited.get(n_arr, -1) == -1:
              if is_in_que.get(n_arr, -1) == -1:
                que.append([n_arr, n_zero_idx])
                is_in_que[n_arr] = 1
  return -1

def list_to_str(arr):
  result = ''
  for i in range(len(arr)):
    result += ''.join(map(str,arr[i]))
  return result

def change(target, a, b):
  tmp = list(target)
  tmp[a], tmp[b] = tmp[b], tmp[a]
  return ''.join(tmp)

arr = [list(map(int,input().split())) for _ in range(3)]
zero = None # 1차원 배열로 치환했을 때의 0 idx
# 0이 숫자 제일 앞자리에 오는 것을 방지하기 위해 0을 9로 바꾸고 idx 저장
for i in range(3):
  for j in range(3):
    if arr[i][j] == 0:
      arr[i][j] = 9
      zero = i * 3 + j
arr = list_to_str(arr) # 1차원 str배열로 치환(2차원 리스트 배열로 하면 시간초과)
print(bfs(arr, zero))

