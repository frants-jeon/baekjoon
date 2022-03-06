##### 단어 수학 #####
import string

'''
자릿수 * 출현 빈도 = 점수
점수가 높은 알파벳 순으로 높은 숫자 할당
각 알파벳을 할당받은 숫자로 변경 후 더하고 출력
'''

N = int(input())
score = [0] * 26 # 알파벳의 점수를 나타낼 리스트
alphabet_list = list(string.ascii_uppercase) # 알파벳 리스트
words = []
for _ in range(N):
  word = input()
  for i in range(len(word)):
    # 단어가 한 번 나올 때마다 자릿수에 해당하는 점수 더해주기
    score[ord(word[i]) - 65] += pow(10, len(word) - 1 - i)
  words.append(word)

# 알파벳과 해당 알파벳의 점수를 묶어주고 점수가 큰 순으로 정렬
ahlphabet_score = sorted(list(zip(alphabet_list, score)), key=lambda x: x[1], reverse=True)
visited_num = [0] * 10 # 사용한 숫자를 체크할 리스트
# 점수가 높은 알파벳 순으로 숫자 변환
for i in range(26):
  if ahlphabet_score[i][1] == 0: break # 점수 순으로 정렬했기 때문에 점수가 없는 알파벳이 나오면 중단
  for num in range(9, -1, -1):
    # 아직 사용하지 않은 숫자라면 방문 배열의 해당 숫자idx자리에 알파벳 할당
    if not visited_num[num]:
      visited_num[num] = ahlphabet_score[i][0]
      break

for i in range(N): # 전체 단어
  for j in range(len(words[i])): # 한 단어
    for num in range(10): # 알파벳 하나
      # 해당 알파벳에 할당된 숫자를 찾으면 숫자로 바꿔줌
      if words[i][j] == visited_num[num]:
        words[i] = words[i].replace(words[i][j], str(num))
        break
answer = sum(map(int, words))
print(answer)