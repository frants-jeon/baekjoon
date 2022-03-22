##### 우수 마을 #####
# https://www.acmicpc.net/problem/1949
from sys import stdin
input = stdin.readline

def dfs(n):
  dp[n][1] = people[n]
  visited[n] = 1

  for child in nodes[n]:
    if not visited[child]:
      dfs(child) # 자식 노드들의 dp값을 먼저 구해주고
      # n번째 마을이 우수마을이면 자식 노드는 우수마을이 아니여야 하기 때문에 해당 경우만 더해주고
      dp[n][1] += dp[child][0]
      # n번째 마을이 우수마을이 아니면 자식노드가 우수마을이든 아니든 최댓값으로 더해준다.
      dp[n][0] += max(dp[child][1], dp[child][0])


N = int(input())
people = [0] + list(map(int,input().split()))
nodes = [[] for _ in range(N + 1)]
for _ in range(N - 1):
  a, b = map(int,input().split())
  nodes[a].append(b)
  nodes[b].append(a)

dp = [[0, 0] for _ in range(N + 1)] # dp[i][j]에서 j=0이면 i번째 마을을 선택 안했을 때, j=1이면 선택했을 때의 최대 인원
visited = [0 for _ in range(N + 1)]

dfs(1)
print(max(dp[1]))