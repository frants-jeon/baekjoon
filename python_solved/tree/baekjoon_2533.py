##### 사회망 서비스(SNS) #####
# https://www.acmicpc.net/problem/2533
from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(1000000)

def sns(n):
  visited[n] = 1
  for child in nodes[n]:
    if not visited[child]:
      sns(child) # 자식 노드들의 값들을 먼저 구해주고
      # n번째 노드가 얼리어답터인 경우에는 자식 노드가 얼리어답터이든 아니든 최솟값을 더해주고
      dp[n][1] += min(dp[child])
      # n번째 노드가 얼리어답터가 아닌 경우에는 모든 자식 노드가 얼리어답터여야 하기 때문에 해당 경우를 더해준다.
      dp[n][0] += dp[child][1]

N = int(input())
nodes = [[] for _ in range(N + 1)] # i번째 노드와 연결된 노드 저장
visited = [0 for _ in range(N + 1)] # i번째 노드 방문 여부 저장
# dp[i][0]은 i번째 노드를 루트로 하는 트리에서 i가 얼리어답터가 아닐 때, dp[i][1]은 얼리어답터일 때에 필요로 하는 총 얼리어답터의 수
dp = [[0, 1] for _ in range(N + 1)]
# 트리 관계 입력
for _ in range(N - 1):
  a, b = map(int,input().split())
  nodes[a].append(b)
  nodes[b].append(a)

sns(1)
print(min(dp[1]))