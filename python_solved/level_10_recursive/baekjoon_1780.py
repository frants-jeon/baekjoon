import sys


N = int(input())
l = []
total = []
for _ in range(N):
    # N 개의 리스트 추가
    l.append(list(map(int,sys.stdin.readline().split())))


def cnt_paper(x, y, n):
    check = l[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if l[i][j] != check:
                check = 'x'
                break
    if check != 'x':
        return total.append(check)

    n = n // 3
    cnt_paper(x, y, n)
    cnt_paper(x, y + n, n)
    cnt_paper(x, y + n * 2, n)
    cnt_paper(x + n, y, n)
    cnt_paper(x + n, y + n, n)
    cnt_paper(x + n, y + n * 2, n)
    cnt_paper(x + n * 2, y, n)
    cnt_paper(x + n * 2, y + n, n)
    cnt_paper(x + n * 2, y + n * 2, n)


cnt_paper(0, 0, N)
cnt_0 = 0
cnt_1 = 0
cnt_m1 = 0
for i in total:
    if i == 0:
        cnt_0 += 1 
    elif i == 1:
        cnt_1 += 1 
    else:
        cnt_m1 += 1 
print(cnt_m1)
print(cnt_0)
print(cnt_1)