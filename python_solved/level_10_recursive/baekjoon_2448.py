##### 별 찍기 - 11 #####
N = int(input())
l = [[' '] * (2 * N - 1) for _ in range(N)]
def star(n, r, c):
    if n == 3:
        l[r][c]='*'
        l[r + 1][c - 1] = '*'
        l[r + 1][c + 1] = '*'
        l[r + 2][c - 2] = '*'
        l[r + 2][c - 1] = '*'
        l[r + 2][c] = '*'
        l[r + 2][c + 1] = '*'
        l[r + 2][c + 2] = '*'
        print(n, r, c)
        return 
    n = int(n / 2)
    star(n, r, c)
    star(n, r + n, c - n)
    star(n, r + n, c + n)


star(N, 0, N - 1)
for i in range(len(l)):
    print(''.join(l[i]))