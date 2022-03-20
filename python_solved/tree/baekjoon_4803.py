##### 트리 #####
# https://www.acmicpc.net/problem/4803

from sys import stdin
input = stdin.readline

def is_tree(i, visited):
  # 이미 방문한 적이 있으면 트리가 아니므로 False
  if visited[i]: return False

  visited[i] = True # 방문처리 해주고
  if i > n or not nodes[i]: return True
  children = nodes[i] # i번째 노드의 자식 노드
  res = True
  for child in children:
    res *= is_tree(child, visited)
  return res


case = 1
while 1:
  n, m = map(int,input().split())
  if n == m == 0:
    break
  nodes = [[] for _ in range(n + 1)]
  # 1번 노드부터 순서대로 들어오기 때문에 자식 노드만 저장
  for _ in range(m):
    a, b = map(int,input().split())
    nodes[a].append(b)
  
  tree = 0
  visited = [0] * (n + 1)
  for i in range(1, n + 1):
    tree += is_tree(i, visited)
  
  if tree == 0:
    print(f'Case {case}: No trees.')
  elif tree == 1:
    print(f'Case {case}: There is one tree.')
  else:
    print(f'Case {case}: A forest of {tree} trees.')
  case += 1

