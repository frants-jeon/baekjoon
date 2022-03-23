##### 트리의 지름 #####
# https://www.acmicpc.net/problem/1967
from sys import stdin,setrecursionlimit
input = stdin.readline
setrecursionlimit(100000)


def find_deep_node(n, w): # n은 노드 번호, w는 가중치
  global deep_node
  # 만약 자식이 없고 제일 깊은 노드라면 deep_node갱신
  if not children[n]:
    if w > deep_node[1]:
      deep_node = [n, w]
    return

  # 자식들을 돌면서 가중치를 더해줌
  for i in range(len(children[n])):
    find_deep_node(children[n][i], p_to_c[n][i] + w)
  return


def calc_dist(n, w): #n번째 노드부터 모든 노드들을 돌면서 거리 갱신
  global answer
  # 해당 노드를 방문처리 해주고 w가 더 크면 answer 갱신
  visited[n] = 1
  if w > answer:
    answer = w

  # 만약 부모가 있고(루트 노드가 아니고) 부모 노드를 방문한 적이 없으면 부모 노드 탐색
  if parents[n] and not visited[parents[n]]:
    calc_dist(parents[n], c_to_p[n] + w)
  
  if children[n]: # 만약 자식 노드가 있다면
    # 자식 노드를 돌면서 방문한 적이 없는 노드만 탐색
    for i in range(len(children[n])):
      if not visited[children[n][i]]:
        calc_dist(children[n][i], p_to_c[n][i] + w)


N = int(input())
parents = [0 for _ in range(N + 1)] # i번째 노드의 부모 노드 번호 저장
children = [[] for _ in range(N + 1)] # i번째 노드의 자식 노드 번호 저장
p_to_c = [[] for _ in range(N + 1)] # parents에서 children으로 갈 때의 가중치
c_to_p = [0 for _ in range(N + 1)] # children에서 parents로 갈 때의 가중치
# 각 정보들 저장
for _ in range(N - 1):
  parent, child, weight = map(int,input().split())
  parents[child] = parent
  children[parent].append(child)
  p_to_c[parent].append(weight)
  c_to_p[child] = weight

# 루트 노드에서 가장 멀리 떨어져 있는 노드를 구해서 저장
deep_node = [0, 0] # 노드 번호, 길이
find_deep_node(1, 0)

# 최대 길이를 갱신할 answer와 방문여부를 체크할 visited 할당
answer = 0
visited = [0 for _ in range(N + 1)]
calc_dist(deep_node[0], 0) # deep_node에서부터 제일 거리가 먼 노드까지의 거리 갱신

print(answer)