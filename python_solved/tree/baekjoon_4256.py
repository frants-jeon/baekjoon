##### 트리 #####
# https://www.acmicpc.net/problem/4256
from sys import stdin
input = stdin.readline

def postorder(inorder):
  global i
  if not inorder: return
  root = preorder[i] # 현재 탐색중인 트리의 루트
  in_root_idx = inorder.index(root) # 중위순회 결과에서 루트노드가 몇번째 인덱스인지
  # 루트노드를 중심으로 좌우로 나눠서 왼쪽자식, 오른쪽 자식으로 구분
  left_child = inorder[:in_root_idx]
  right_child = inorder[in_root_idx + 1:]
  i += 1 # 자식들을 찾았으니 전위순회 결과의 다음 노드를 탐색

  # 후위순회를 하기 위해 왼쪽자식 돌고 오른쪽 자식 돌고 루트를 리스트에 추가
  postorder(left_child)
  postorder(right_child)
  answer.append(root)


for tc in range(int(input())):
  N = int(input())
  preorder = list(map(int,input().split())) # 전위순회 결과
  inorder = list(map(int,input().split())) # 중위순회 결과
  i = 0 # 전위순회 결과의 몇번째 인덱스 탐색 중인지 표시
  answer = []
  postorder(inorder)
  print(*answer)