##### 바이러스 #####
# https://www.acmicpc.net/problem/2606
from sys import stdin
input = stdin.readline

N = int(input())
cnt = -1
tree = [[] for _ in range(N + 1)]
# 트리 입력
for _ in range(int(input())):
  a, b = map(int,input().split())
  tree[a].append(b)
  tree[b].append(a)

visited = [0 for _ in range(N + 1)]
def virus(n):
  global cnt
  # n번 컴퓨터가 바이러스에 감염됨. cnt해주고 자식 노드들 방문하여 감염 진행
  if not visited[n]:
    visited[n] = 1
    cnt += 1
    for child in tree[n]:
      virus(child)

virus(1)
print(cnt)