##### 트리의 높이와 너비 #####
# https://www.acmicpc.net/problem/2250
from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(100000)
# ------- 필요한 변수 생성 ------
N = int(input())
left_child = [0 for _ in range(N + 1)] # i번째 노드의 왼쪽 자식노드 번호 저장
right_child = [0 for _ in range(N + 1)] # i번째 노드의 오른쪽 자식노드 번호 저장
level_width = dict() # n번째 레벨(뎁스)의 너비 저장
root = {i for i in range(1, N + 1)} # 루트 노드 구하기 위한 set
width = 1 # 현재 노드의 열 번호 저장

# ------ 인풋 받아서 할당 & 루트 찾기 -----
for _ in range(N):
  # 왼쪽자식, 오른쪽 자식 번호 할당하고
  node, left, right = map(int,input().split())
  left_child[node] = left
  right_child[node] = right
  # node의 자식들은 root가 아니기 때문에 root 후보군에서 제거
  if left != -1:
    root.remove(left)
  if right != -1:
    root.remove(right)

# 현재 레벨의 너비 구하기
def check_width(level):
  global width
  val = level_width.get(level, -1)
  # 현재 레벨의 너비를 구한적이 없으면 [최솟값, 최댓값] 모두 현재 width로 할당
  if val == -1:
    level_width[level] = [width, width]
  # 왼쪽에서 오른쪽으로 점점 width가 커지기 때문에 이미 구한적 있으면 최댓값만 갱신
  else:
    level_width[level][1] = width
  width += 1

# 격자에 트리 그리기. 중위 순회(왼쪽자식, 루트, 오른쪽 자식)
def drawing_tree(n, level):
  if n == -1: return
  drawing_tree(left_child[n], level + 1)
  check_width(level)
  drawing_tree(right_child[n], level + 1)
  return

# 루트를 찾았으니 루트부터 레벨1에서 시작해서 레벨별 너비를 구함
drawing_tree(list(root)[0], 1)


answer = [100000, 0] #[level, max_width]
# key = 레벨, val = [width최솟값, 최댓값]
for key, val in level_width.items():
  # key레벨의 너비 구하기
  cur_width = val[1] - val[0] + 1
  # 너비가 max_width이면서 level이 더 낮으면 갱신
  if cur_width == answer[1]:
    if key < answer[0]:
      answer = [key, cur_width]
  # 너비가 max_width보다 더 크면 그냥 갱신
  elif cur_width > answer[1]:
    answer = [key, cur_width]

print(*answer)


