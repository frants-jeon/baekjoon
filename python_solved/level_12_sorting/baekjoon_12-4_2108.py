import sys

N = int(sys.stdin.readline())
li = []
for _ in range(N):
    li.append(int(sys.stdin.readline()))
li.sort()

cnt_li = {}
for num in li:
    if num in cnt_li:
        cnt_li[num] += 1
    else:
        cnt_li[num] = 1


max_cnt = []
for key, value in cnt_li.items():
    if value == max(cnt_li.values()):
        max_cnt.append(key)


if len(max_cnt) == 1:
    frequent = max_cnt[0]
else:
    max_cnt.remove(min(max_cnt))
    frequent = min(max_cnt)


average = int(round(sum(li) / N,0))
mid = li[(len(li) - 1)//2]
num_range = max(li) - min(li)
print(average, mid, frequent, num_range, sep='\n')
