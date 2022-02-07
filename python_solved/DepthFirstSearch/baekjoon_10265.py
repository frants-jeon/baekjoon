##### MT #####
from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(200000)

def dfs(idx):
  global cnt, getOn
  # 이미 방문이 완전히 끝났으면 그냥 종료
  if finished[idx]: return
  # 만약 방문을 안했었다면
  if not visited[idx]:
    #방문 여부를 True로 바꾸고 이어서 탐색
    visited[idx] = 1
    dfs(students[idx])
    # 바라보는 학생이 사이클 안에 있거나 사이클을 바라보고 있으면(사이클에 포함된 학생이 버스에 타야) idx번 학생도 탈 수 있음
    # 그러나 이미 finished 됐기 때문에 for문 돌면서 체크해 줌
    for i in range(len(cycles)):
      if students[idx] in cycles[i] or students[idx] in stacks[i]:
        stacks[i].append(idx)
        # stack에 이미 추가된 학생은 dfs밖에서 다시 추가되지 않기 위해 getOn 변수 사용
        getOn = False
        break
    stack.add(idx)
    # 탐색을 끝내고 돌아왔으면 방문 마무리 여부 True로 바꾸고 종료
    finished[idx] = 1
    return
  # 방문은 했었는데 끝난게 아니라면(사이클 성립)
  if visited[idx] and not finished[idx]:
    # 사이클이니까 카운트 늘려주고 다시 사이클 한 바퀴 더 돌았을 때 종료되도록 방문 마무리 True로 바꿔주고 한 바퀴 더 돌고 종료
    finished[idx] = 1
    cycle.add(idx)
    dfs(students[idx])
    return

n, k = map(int,input().split())
students = ['0'] + list(map(int,input().split()))
visited = ['0'] + [0] * n
finished = ['0'] + [0] * n
cnt = 0
cycles = [] # 컴포넌트마다 사이클에 포함된 인원
stacks = [] # 컴포넌트마다 사이클에 포함되지 않는 인원

for i in range(1, n + 1):
  # 중복된 노드를 빼주기 위해 set으로 설정
  stack = set()
  cycle = set()
  getOn = True
  dfs(i)
  if stack and getOn:
    stacks.append(list(stack - cycle))
  if cycle:
    cycles.append(list(cycle))

# arr를 각 노드별 개수로 다시 지정. ex) [[1,5,3,2],[6,7]...] -> [[4, 2]...]
newArr = [0] + sorted([[len(cycles[i]), len(stacks[i])] for i in range(len(cycles))])
dp = [[-1] * (k + 1) for _ in range(len(newArr))]


def bus(idx, left): # idx = idx번째 컴포넌트. left = 현재 조건에서 태울 수 있는 사람 수(버스에 남은 자리)
  if idx == 0 or left == 0: return 0 # 종료 조건 설정
  if dp[idx][left] != -1: return dp[idx][left] # 이미 구해놓은 값이면 해당 값 리턴

  # idx번째 사이클이 더 커서 현재 컴포넌트는 태울 수 없는 경우
  if newArr[idx][0] > left:
    dp[idx][left] = bus(idx - 1, left) # 이전 컴포넌트 값과 동일
    return dp[idx][left]
  
  # 현재 컴포넌트에서 태울 수 있는 경우
  cycle_number = newArr[idx][0]
  total_number = sum(newArr[idx])
  ans = bus(idx - 1, left)
  # 사이클부터 컴포넌트 전체 크기만큼 돌면서 최댓값 갱신
  for l in range(cycle_number, total_number + 1):
    if l > left: break
    ans = max(ans, bus(idx -1, left - l) + l)
  dp[idx][left] = ans
  return dp[idx][left]

print(bus(len(newArr) - 1, k))
