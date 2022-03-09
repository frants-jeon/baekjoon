##### 트리의 부모 찾기 #####
# https://www.acmicpc.net/problem/11725

from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(200000)

N = int(input())
nodes = [[] for _ in range(N + 1)]
parents = [0 for _ in range(N + 1)]
for _ in range(N - 1):
  a, b = map(int,input().split())
  nodes[a].append(b)
  nodes[b].append(a)

def dfs(start, parents):
  for i in nodes[start]:
    if parents[i] == 0:
      parents[i] = start
      dfs(i, parents)

dfs(1, parents)
for i in range(2, N + 1):
  print(parents[i])