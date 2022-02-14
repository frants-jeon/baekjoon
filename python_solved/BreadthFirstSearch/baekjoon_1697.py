##### 숨바꼭질 #####
from collections import deque


def bfs(start, end):
  que = deque([start])
  visited = [0] * 100001
  cnt = 0

  while que:
    cnt += 1
    for _ in range(len(que)):
      node = que.popleft()
      # 노드를 방문한 적이 없으면 방문 처리 후 탐색
      if not visited[node]:
        visited[node] = cnt
        for i in [node + 1, node -1, node * 2]:
          if 0 <= i < 100001:
            if not visited[i]:
              que.append(i)
    if visited[end]: break

  return cnt - 1

N, K = map(int,input().split())
print(bfs(N, K))
