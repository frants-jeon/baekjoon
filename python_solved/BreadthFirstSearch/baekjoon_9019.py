##### DSLR #####
from collections import deque

def bfs(start, goal):
  que = deque([[start, -1]])
  # que에 이미 있는 것을 다시 넣지 않기 위해 que에 있는지 여부를 확인할 리스트 생성
  que_list = [0] * 10000

  while que:
    num, order = que.popleft()
    que_list[num] = 0 # que에서 빠졌다고 체크
    # 방문한 적이 없으면 방문처리 하고 탐색 시작
    if not visited[num]:
      visited[num] = order
      if num == goal: break # 방문한 값이 최종값과 동일하면 break
      # 각 명령어를 수행했을 때 생성되는 값 계산
      D = (num * 2) % 10000
      S = (num + 9999) % 10000
      L = (num * 10) % 10000 + num // 1000
      R = (num // 10) + (num % 10) * 1000
      # new_num은 각 명령어를 수행했을 때의 값
      # new_order는 다섯자리로 구성하여 뒷 네자리는 명령어 수행 전의 숫자이고 첫자리는 DSLR 순으로 1,2,3,4로 함. str은 느리기 때문에 int로 해결.
      for new_num, new_order in [[D, 10000], [S, 20000], [L, 30000], [R, 40000]]:
        # 방문한 적이 없고 큐에도 없으면 큐에 추가
        if not visited[new_num] and not que_list[new_num]:
          que.append([new_num, new_order + num])
          que_list[new_num] = 1
        # 최종값이 큐에 있으면 최종 값을 큐의 제일 앞으로 옮겨줌.
        if que_list[goal]:
          que.rotate(-(len(que) - 1))
          break

  backtracking(goal)

# target은 명령어 수행 전의 숫자와 어떤 명령을 수행했는지 알고 싶은 값. 역추적으로 답 도출.
def backtracking(target):
  # visited[start]의 값(A의 값)은 -1로 해뒀기 때문에 처음 숫자까지 역추적 했으면 리턴
  if visited[target] == -1: return
  
  # 10,000으로 나눈 몫 = 수행한 명령이고 나머지는 수행 이전의 숫자.
  order, before_num = divmod(visited[target], 10000)
  # 어떤 명령어를 수행했는지 확인해서 ol(수행한 명령어 리스트)에 추가하고 이어서 탐색
  if order == 1:
    ol.appendleft('D')
    backtracking(before_num)
  elif order == 2:
    ol.appendleft('S')
    backtracking(before_num)
  elif order == 3:
    ol.appendleft('L')
    backtracking(before_num)
  elif order == 4:
    ol.appendleft('R')
    backtracking(before_num)


for tc in range(int(input())):
  A, B = map(int,input().split())
  visited = [0] * 10000
  ol = deque() # 수행한 명령어 리스트
  bfs(A, B)
  print(''.join(ol))