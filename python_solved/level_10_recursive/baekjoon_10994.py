N = int(input())
l = []
for _ in range((N - 1) * 4 + 1):
    l1 = []
    l.append(l1)
    for _ in range((N - 1) * 4 + 1):
        l1.append(' ')
def star(n, r, c):
    size = (n - 1) * 4 + 1
    if n == 1:
        l[r][c] = '*'
        return
    for i in range(size):
        l[r][c + i] = '*'
        l[len(l) - r - 1][c + i] = '*'
        l[r + i][c] = '*'
        l[r + i][len(l) - c - 1] = '*'

    star (n - 1, r + 2, c + 2)

star(N, 0, 0)
for i in range(len(l)):
    star_print = ''
    star_print += ''.join(l[i])
    print(star_print)