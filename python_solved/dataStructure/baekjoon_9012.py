##### 괄호 #####
from sys import stdin
input = stdin.readline

for _ in range(int(input())):
  stack = []
  data = input().strip()
  for i in data:
    # 괄호를 열면 스택에 추가
    if i == '(':
      stack.append(i)
    # 닫는 괄호인데 스택에 여는 괄호가 있으면 닫아주기 위해 pop
    elif stack:
      stack.pop()
    # 닫는 괄호인데 스택이 비어있으면 잘못된 괄호니까 break
    else: stack = 'NO'; break
  # 스택이 비어있어야 YES
  if stack: print('NO')
  else: print('YES')
