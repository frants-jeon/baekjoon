##### 색종이 만들기 #####
import sys

N = int(input())
paper = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
cnt_0 = 0
cnt_1 = 0

def div_paper(n, l: list):
    global cnt_0
    global cnt_1
    check = 0
    for i in range(n):
        for j in range(n):
            if l[i][j] == 1:
                check += 1
    # 전체 개수와 1의 개수가 같으면 1의 개수 +
    if check == n ** 2:
        cnt_1 += 1
        return
    # 1의 개수가 0이면 0의 개수 +
    elif check == 0:
        cnt_0 += 1
        return
    
    quadrant_1 = []
    quadrant_2 = []
    quadrant_3 = []
    quadrant_4 = []


    for i in range(n // 2):
        quadrant_1.append(l[i][:n // 2])
        quadrant_2.append(l[i][n // 2: ])
    for i in range(n // 2, n):
        quadrant_3.append(l[i][:n // 2])
        quadrant_4.append(l[i][n // 2: ])
    


    div_paper(n // 2, quadrant_1)
    div_paper(n // 2, quadrant_2)
    div_paper(n // 2, quadrant_3)
    div_paper(n // 2, quadrant_4)


div_paper(N, paper)
print(cnt_0)
print(cnt_1)