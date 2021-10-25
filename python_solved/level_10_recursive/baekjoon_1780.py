import sys


N = int(input())
l = []
total = []
for _ in range(N):
    # N 개의 리스트 추가
    l.append(list(map(int,sys.stdin.readline().split())))
print(l)
print('')

def cnt_paper(n, l):
    cnt_0 = 0
    cnt_1 = 0
    cnt_m1 = 0
    for i in l:
        for j in i:
            if j == 0:
                cnt_0 += 1
            elif j == 1:
                cnt_1 += 1
            else:
                cnt_m1 += 1
    if cnt_0 == 0 and cnt_1 == 0:
        return total.append(-1)
    elif cnt_0 == 0 and cnt_m1 == 0:
        return total.append(1)
    elif cnt_1 == 0 and cnt_m1 == 0:
        return total.append(0)

    m = [[] * x for x in range(9)]
    # m = [[[] * x for x in range(n // 3)]] * 9
    for i in range(n // 3):
        for j in range(n // 3):
            m[0].append(l[i][j])
            print(m[0])
        for j in range(n // 3, n * 2 // 3):
            m[1].append(l[i][j])
        for j in range(n * 2 // 3, n):
            m[2].append(l[i][j])
        
        

    for i in range(n // 3, n * 2 // 3):
        for j in range(n // 3):
            m[3].append(l[i][j])
        for j in range(n // 3, n * 2 // 3):
            m[4].append(l[i][j])
        for j in range(n * 2 // 3, n):
            m[5].append(l[i][j])

    for i in range(n * 2 // 3, n):
        for j in range(n // 3):
            m[6].append(l[i][j])
        for j in range(n // 3, n * 2 // 3):
            m[7].append(l[i][j])
        for j in range(n * 2 // 3, n):
            m[8].append(l[i][j])
    
    print(m)
    for i in range(9):
        cnt_paper(n // 3, m[i])


cnt_paper(N, l)
print(total)