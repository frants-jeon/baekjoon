##### 트리 #####
# https://www.acmicpc.net/problem/1068

def remove_node(n):
  global answer
  # n번째 노드 삭제 시 n번째 노드는 리프노드가 아니라고 표시
  answer[n] = 0
  # n번째 노드의 자식을 돌면서 하위 노드들도 삭제
  for child in children[n]:
    remove_node(child)


N = int(input())
parents = list(map(int,input().split())) # i번째 노드의 부모 표시
target = int(input())
children = [[] for _ in range(N)]
# i번째 노드의 자식 표시
for i in range(N):
  if parents[i] == -1: continue # -1의 자식을 찾으면 N - 1의 자식을 또 찾으므로 패스
  children[parents[i]].append(i)

# i번째 노드가 리프 노드라면 1, 아니면 0 표시
answer = [1 if not children[i] else 0 for i in range(N)]
remove_node(target) # 타겟 노드 삭제
# 타겟 노드가 부모의 유일한 자식이였을 경우, 부모 노드가 리프노드가 되므로 이런 케이스에 해당한다면 + 1해서 출력
print(sum(answer) if len(children[parents[target]]) != 1 else sum(answer) + 1)
