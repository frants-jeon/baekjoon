##### 양 구출 작전 #####
# https://www.acmicpc.net/problem/16437
from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(200000)

# n번째 섬까지 도착한 양이 몇마리인지 세어주는 함수
def move_sheep(n):
  # 이동할 양이 없으면 0 리턴
  if sheep[n] == 0: return 0
  # 자식이 없고 해당 섬에 양이 있으면 양의 수 리턴
  if not children[n]:
    if sheep[n] > 0:
      return sheep[n]
  
  # 자식이 있으면 자식섬에서 n번 섬으로 양 이동
  for child in children[n]:
    tmp = move_sheep(child) # 자식섬에 있는 양의 수
    if tmp < 0: continue # 음수라면 늑대이므로 패스
    # 자식 섬에서 n번 섬으로 양이 이동하기 때문에 자식 섬은 0마리로 바꿔주고 n번 섬에 더하기
    sheep[child] = 0
    sheep[n] += tmp
  return sheep[n]


N = int(input())
sheep = [0 for _ in range(N + 1)]
children = [[] for _ in range(N + 1)]
# i번째 섬의 자식 섬 번호와 양의 수 할당. 늑대는 마이너스로 표시
for i in range(2, N + 1):
  who, many, to = input().split()
  children[int(to)].append(i)
  sheep[i] = int(many)
  if who == 'W':
    sheep[i] *= -1

sheep[1] = 1
move_sheep(1)
print(sheep[1] - 1)