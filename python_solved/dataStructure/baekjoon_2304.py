##### 창고 다각형 #####
from sys import stdin
input = stdin.readline

N = int(input())
pillars = [list(map(int,input().split())) for _ in range(N)]
pillars.sort(key=lambda x: x[0]) # x좌표 순으로 정렬
highestIdx = pillars.index(max(pillars, key=lambda x: x[1])) # 제일 높은 기둥 인덱스
# 높은 기둥을 기준으로 좌우의 넓이를 구해주고 높은 기둥의 넓이를 따로 더해주는 방식으로 진행하기 위해 answer에 미리 높은 기둥의 넓이를 담아줌
answer = pillars[highestIdx][1]

# 지붕과 닿아있는 기둥을 stack에 저장
stack = [pillars[0]]
# 제일 높은 기둥 전까지의 넓이 구하기
for i in range(1, highestIdx + 1):
  # 지금 비교할 기둥이 스택의 기둥보다 크거나 최대 높이면
  if pillars[i][1] > stack[-1][1] or pillars[i][1] == pillars[highestIdx][1]:
    high = stack.pop()
    # 지금까지의 넓이를 구해서 더해주고 stack에 추가
    answer += (pillars[i][0] - high[0]) * high[1]
    stack.append(pillars[i])

stack = [pillars[-1]]
# 앞과 동일
for j in range(N - 2, highestIdx - 1, - 1):
  if pillars[j][1] > stack[-1][1] or pillars[j][1] == pillars[highestIdx][1]:
    high = stack.pop()
    answer += (high[0] - pillars[j][0]) * high[1]
    stack.append(pillars[j])

print(answer)

