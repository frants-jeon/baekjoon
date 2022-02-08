##### DFS와 BFS #####
from sys import stdin, setrecursionlimit
from collections import deque
input = stdin.readline
setrecursionlimit(20000)

def dfs(node):
  if node in dfs_answer: return # 이미 방문한 노드면 종료
  dfs_answer.append(node) # 새로 방문한 노드는 answer에 추가
  # 노드와 이어진 노드는 dfs 진행
  for i in arr[node]:
    dfs(i)

def bfs(start):
  que = deque([start])
  answer = []

  while que:
    node = que.popleft()
    # 방문한 적이 없는 노드는 answer에 추가 후 이어진 노드는 que에 추가하여 bfs진행
    if node not in answer:
      answer.append(node)
      que.extend(arr[node])

  return answer

N, M, V = map(int,input().split())
arr = [[0]] + [[] for _ in range(N)]

# 양방향 그래프이므로 서로 이어진 노드 모두에 서로 추가
for _ in range(M):
  tmp = list(map(int,input().split()))
  arr[tmp[0]].append(tmp[1])
  arr[tmp[1]].append(tmp[0])

# 번호가 빠른 노드 먼저 방문하므로 정렬
for i in range(1, N + 1):
  arr[i] = sorted(arr[i])


dfs_visited = [0] * (N + 1)
dfs_answer = []

# 양식에 맞게 출력
dfs(V)
print(' '.join(map(str,dfs_answer)))
print(' '.join(map(str,bfs(V))))