##### 후위 표기식2 #####
from sys import stdin
import string
input = stdin.readline

N = int(input())
cal = input().strip()
# 알파벳 순서대로 숫자를 매칭하기 때문에 idx가 매치되도록 numList와 알파벳 리스트 생성
numList = [int(input()) for _ in range(N)]
alphabet = list(string.ascii_uppercase)
# 숫자를 넣어줄 스택 생성
stack = []
for i in cal:
  # 연산자일 경우 stack에서 두 개를 빼서 연산 후 다시 stack에 추가
  if i in '*/+-':
    b = stack.pop()
    a = stack.pop()
    if i == '*':
      stack.append(a * b)
    elif i == '/':
      stack.append(a / b)
    elif i == '+':
      stack.append(a + b)
    else: stack.append(a - b)
  # 피연산자면 해당 알파벳 인덱스를 numList에서 찾아서 stack에 추가
  else:
    stack.append(numList[alphabet.index(i)])
print(f'{stack[0]:.2f}')