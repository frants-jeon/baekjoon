##### 촌수계산 #####
from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())
# 서로 촌수를 비교할 a와 b입력
a, b = map(int,input().split())
m = int(input())
# idx번째 사람의 부모,자식 번호를 저장할 배열 생성
relation = [[] for _ in range(n + 1)]
# a번 사람과의 촌수를 저장할 배열 생성
result = [0] * (n + 1)
for _ in range(m):
  tmp = list(map(int,input().split()))
  relation[tmp[0]].append(tmp[1])
  relation[tmp[1]].append(tmp[0])


def bfs(start):
  que = deque([start])
  visited = [0] * (n + 1)
  visited[start] = 1

  # 큐가 비어있을 때까지 반복
  while que:
    # 큐에서 빼서 노드 탐색
    node = que.popleft()
    # 노드와 연결되어 있는 컴포넌트 탐색
    for i in relation[node]:
      # 방문한 적이 없으면 방문처리하고 큐에 추가
      if not visited[i]:
        visited[i] = 1
        que.append(i)
        # i는 노드와 1촌 차이. 결과 저장
        result[i] = result[node] + 1
  
bfs(a)
print(result[b] if result[b] != 0 else -1)