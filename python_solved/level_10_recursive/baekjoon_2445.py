N = int(input())

def star_print(star, total):
    print('*' * star,end='')
    print(' ' * (total * 2 - star * 2),end='')
    print('*' * star)


for i in range(1, N + 1):
    star_print(i, N)
for i in range(N - 1, 0, -1):
    star_print(i, N)