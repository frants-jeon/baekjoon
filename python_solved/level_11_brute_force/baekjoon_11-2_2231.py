##### 분해합 #####
N = int(input())
if N > 55:
    is_answer = N - 54
else:
    is_answer = 1
answer = False
for i in range(is_answer, N):
    separate = [i]
    s = str(i)
    for j in s:
        separate.append(int(j))
    if sum(separate) == N:
        answer = True
        break

if answer:
    print(i)
else:
    print(0)