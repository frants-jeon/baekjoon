##### 잃어버린 괄호 #####
from sys import stdin
formula = stdin.readline()
tmp = ''
num_list = []
sign_list = []
for i in range(len(formula)):
  if formula[i] == '-' or formula[i] == '+':
    num_list.append(int(tmp))
    tmp = ''
    num_list.append(formula[i])
  else:
    tmp += formula[i]
num_list.append(int(tmp))

try:
  minus_idx = num_list.index('-')
  answer = sum([num_list[x] for x in range(0, minus_idx, 2)]) - sum([num_list[y] for y in range(minus_idx + 1, len(num_list), 2)])
except:
  answer = sum([num_list[x] for x in range(0, len(num_list), 2)])
print(answer)