n = int(input())
a = 0
for i in range(n):
    a = a + 1
    b = n - a
    print(' ' * b,'*' * a, sep='')