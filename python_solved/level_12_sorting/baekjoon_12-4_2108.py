##### 통계학 #####
from sys import stdin
input = stdin.readline

N = int(input())
li = sorted([int(input()) for _ in range(N)])

cnt_dict = {} # key = num, value = num이 나온 횟수
frequency_cnt = 1 # 제일 빈번하게 나온 횟수
frequency_num_list = [] # 빈번하게 나온 수 리스트
for num in li:
  # 이미 dict에 있으면 횟수 더해줌
  if cnt_dict.get(num, '0') != '0':
    cnt_dict[num] += 1
    num_cnt = cnt_dict[num]
    # 현재값이 기존 최빈값과 같으면 최빈값 리스트에 추가
    if frequency_cnt == num_cnt:
      frequency_num_list.append(num)
    # 현재값이 새로운 최빈값이면 횟수 갱신하고 리스트 리셋
    elif frequency_cnt < num_cnt:
      frequency_cnt = num_cnt
      frequency_num_list = [num]
  else: # dict에 없는 경우에는 최빈 횟수가 1인 경우만 추가
    cnt_dict[num] = 1
    if frequency_cnt == 1:
      frequency_num_list.append(num)

frequency = frequency_num_list[0] if len(frequency_num_list) == 1 else sorted(frequency_num_list)[1]
average = int(round(sum(li) / N,0))
mid = li[(len(li) - 1)//2]
print(average)
print(mid)
print(frequency)
print(li[-1] - li[0])