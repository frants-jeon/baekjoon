##### 좋은 단어 #####
from sys import stdin
input = stdin.readline

N = int(input())
words = [input().strip() for _ in range(N)]
cnt = 0
# 각 테스트 케이스를 돌면서
for word in words:
  stack = []
  for i in word:
    # 문자가 stack에 있고 stack의 top이 i면 제거 (그냥 stack[-1] == i라고 하면 빈 스택에서 에러)
    if i in stack and stack[-1] == i:
      stack.pop()
    # 아니면 추가
    else: stack.append(i)
  # 스택이 비어있으면 좋은 단어
  if not stack: cnt += 1
print(cnt)