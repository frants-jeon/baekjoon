##### 후위 표기식 #####
from sys import stdin
input = stdin.readline

formula = input().strip()
stack = []
answer = ''
for i in formula:
  # 기호를 만나면
  if i in '+-*/()':
    # 연산 우선순위가 높은 */ 일때
    if i in '*/':
      # stack이 비어있지 않는 동안
      while stack:
        # 같은 우선순위인데 먼저 들어있던 것을 출력
        if stack[-1] in '*/':
          answer += stack.pop()
        else: break
      # 우선순위가 아닌 것만 남았을 때 stack에 추가
      stack.append(i)
    elif i in '+-':
      while stack:
        if stack[-1] == '(': break
        answer += stack.pop()
      stack.append(i)
    # 여는 괄호는 넣어주고
    elif i == '(': stack.append(i)
    # 닫는 괄호를 만나면 '('가 나올 때까지 빼서 출력해주고 '('를 만나면 멈춤
    else:
      while 1:
        top = stack.pop()
        if top == '(': break
        answer += top
  else: answer += i
# 스택에 남아있는 것들을 차례로 출력
while stack:
  answer += stack.pop()
print(answer)