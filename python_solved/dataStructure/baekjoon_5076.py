##### Web pages #####
from sys import stdin
input = stdin.readline

def check_tag(sentence):
  stack = []
  while sentence != '' and sentence.find('>') != -1:
    tagOpenIdx = sentence.find('<')
    spaceIdx = sentence.find(' ')
    tagCloseIdx = sentence.find('>')
    # 단일 태그인 경우 stack에 추가 없이 넘어감
    if sentence[tagCloseIdx - 1] == '/':
      sentence = sentence[tagCloseIdx + 1:].strip()
      continue
    # 현재 제일 앞에 있는 태그 이름 변수 할당
    if tagOpenIdx < spaceIdx < tagCloseIdx:
      tagName = sentence[tagOpenIdx + 1: spaceIdx]
    else:
      tagName = sentence[tagOpenIdx + 1:tagCloseIdx].strip('/')
    # 여는 태그인 경우 stack에 추가
    if sentence[tagOpenIdx + 1] != '/':
      stack.append(tagName)
    # 닫는 태그면서 stack의 top이랑 같으면 pop
    elif stack and stack[-1] == tagName: # 인덱스 에러 방지하기 위해 스택이 차있다는 조건 추가
      stack.pop()
    else: stack.append(tagName)
    sentence = sentence[tagCloseIdx + 1:].strip()
  
  if stack: return 'illegal'
  else: return 'legal'



while 1:
  line = input().strip()
  # '#'이 나오면 종료
  if line == '#': break
  # tag가 없이 문자열만 있으면 ligal 출력
  if line.find('<') == -1:
    print('legal')
    continue
  print(check_tag(line))