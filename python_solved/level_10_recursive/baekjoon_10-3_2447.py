N = int(input())
l = []
for _ in range(N):
    line = []
    l.append(line)
    for _ in range(N):
        line.append(' ')


# 별 찍는 재귀 함수
def print_star(n, r, c):
    if n == 3:
        l[r][c] = '*'
        l[r][c + 1] = '*'
        l[r][c + 2] = '*'
        l[r + 1][c] = '*'
        l[r + 1][c + 2] = '*'
        l[r + 2][c] = '*'
        l[r + 2][c + 1] = '*'
        l[r + 2][c + 2] = '*'
        return
    
    n = int(n / 3)
    print_star(n, r, c)
    print_star(n, r, c + n)
    print_star(n, r, c + n * 2)
    print_star(n, r + n, c)
    print_star(n, r + n, c + n * 2)
    print_star(n, r + n * 2, c)
    print_star(n, r + n * 2, c + n)
    print_star(n, r + n * 2, c + n * 2)



print_star(N,0,0)
for i in range(len(l)):
    print(''.join(l[i]))






























# def draw_star(n) :
#     global Map
    
#     if n == 3 :
#         Map[0][:3] = Map[2][:3] = [1]*3
#         Map[1][:3] = [1, 0, 1]
#         return

#     a = n//3
#     draw_star(a)
#     for i in range(3) :
#         for j in range(3) :
#             if i == 1 and j == 1 :
#                 continue
#             for k in range(a) :
#                 Map[a*i+k][a*j:a*(j+1)] = Map[k][:a] # 핵심 아이디어

# N = int(input())      

# # 메인 데이터 선언
# Map = [[0 for i in range(N)] for i in range(N)]

# draw_star(N)

# for i in Map :
#     for j in i :
#         if j :
#             print('*', end = '')
#         else :
#             print(' ', end = '')
#     print()


