##### 텀 프로젝트 #####
from sys import stdin, setrecursionlimit
setrecursionlimit(1000000)
input = stdin.readline

def dfs(idx):
  global cnt
  # 이미 방문이 완전히 끝났으면 그냥 종료
  if finished[idx]: return
  # 만약 방문을 안했었다면
  if not visited[idx]:
    #방문 여부를 True로 바꾸고 이어서 탐색
    visited[idx] = 1
    dfs(students[idx])
    # 탐색을 끝내고 돌아왔으면 방문 마무리 여부 True로 바꾸고 종료
    finished[idx] = 1
    return
  # 방문은 했었는데 끝난게 아니라면(사이클 성립)
  if visited[idx] and not finished[idx]:
    # 사이클이니까 카운트 늘려주고 다시 사이클 한 바퀴 더 돌았을 때 종료되도록 방문 마무리 True로 바꿔주고 한 바퀴 더 돌고 종료
    cnt += 1
    finished[idx] = 1
    dfs(students[idx])
    return


T = int(input())
for _ in range(T):
  n = int(input())
  cnt = 0
  # 학생 번호가 1번부터 시작하므로 idx 1번부터 n번까지 본인이 선택한 학생 리스트 생성
  students = ['0'] + list(map(int,input().split()))
  # 방문 한적 있으면 True(1), 안했으면 False(0)인 배열 생성
  visited = ['0'] + [0] * n
  # 방문이 완전히 끝났으면 True(1), 안끝났으면 False(0)인 배열 생성
  finished = ['0'] + [0] * n

  for i in range(1, n + 1):
    dfs(i)
  print(n - cnt)