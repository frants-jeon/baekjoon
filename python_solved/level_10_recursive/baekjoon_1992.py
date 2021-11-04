import sys

N = int(sys.stdin.readline())
l = []
for _ in range(N):
    # 2차원 배열로 저장
    l.append([sys.stdin.readline().strip('\n')])

def quad_tree(n, l):
    cnt0 = 0
    cnt1 = 0
    for s in l:
        for i in s[0]:
            if i == '0':
                cnt0 += 1
            else:
                cnt1 += 1
    if cnt0 == 0:
        print(1, end='')
    elif cnt1 == 0:
        print(0, end='')

    else:
        # 사분면 리스트 생성
        quadrant1 = []
        quadrant2 = []
        quadrant3 = []
        quadrant4 = []
        # l의 n/2줄까지(1,2사분면) 추가
        for i in range(int(n/2)):
            quadrant1.append([l[i][0][:int(n/2)]]) # i 줄에서 n/2번째 까지 1사분면
            quadrant2.append([l[i][0][int(n/2):]]) # i 줄에서 n/2번째 부터 2사분면
        # l의 n/2줄부터(3,4사분면) 추가
        for i in range(int(n/2),n):
            quadrant3.append([l[i][0][:int(n/2)]]) # i 줄에서 n/2번째 까지 3사분면
            quadrant4.append([l[i][0][int(n/2):]]) # i 줄에서 n/2번째 까지 4사분면
        # (1사분면~4사분면 순으로 출력)
        print('(', end='')
        quad_tree(int(n / 2), quadrant1)
        quad_tree(int(n / 2), quadrant2)
        quad_tree(int(n / 2), quadrant3)
        quad_tree(int(n / 2), quadrant4)
        print(')', end='')
        
quad_tree(N, l)