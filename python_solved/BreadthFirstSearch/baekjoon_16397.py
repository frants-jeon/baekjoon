##### 탈출 #####
from collections import deque

def bfs(num,left_cnt, goal):
  que = deque([num])
  visited = [0] * 100000
  cnt = 0

  while que:
    cnt += 1
    for _ in range(len(que)):
      node = que.popleft()
      # 현재 숫자가 목표 숫자랑 같으면 return
      if node == goal: 
        return cnt - 1
      # 현재 숫자를 방문한 적이 없으면 방문 처리를 해주고
      if not visited[node]:
        visited[node] = cnt
        # 버튼 A, B를 눌렀을 때의 값을 구해주고
        btn_A = node + 1
        twice = node * 2
        btn_B = twice - pow(10, len(str(twice)) - 1)
        # A값이 100,000 미만이고 방문한 적이 없으면 que에 추가
        if btn_A < 100000 and not visited[btn_A]:
          que.append(btn_A)
        # twice가 100,000 미만이고 B값이 0에서 99,999 사이일 때, 방문한 적이 없으면 que에 추가
        if twice < 100000 and 0 <= btn_B < 100000:
          if not visited[btn_B]:
            que.append(btn_B)
    # 남은 횟수가 없으면 탈출 불가
    if left_cnt - cnt + 1 <= 0: return 'ANG'

N, T, G = map(int,input().split())
print(bfs(N, T, G))


"""
0 99999 99999
answer = 11198
"""