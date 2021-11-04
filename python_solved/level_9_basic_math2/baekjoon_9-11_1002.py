import math

T = int(input())
for _ in range(T):
    x_1, y_1, r_1, x_2, y_2, r_2 = map(int,input().split())
    d = abs(x_1 - x_2) ** 2 + abs(y_1 - y_2) ** 2
    print(d)
    print((r_1 + r_2) ** 2)
    print(r_1 ** 2 + r_2 ** 2)
    if x_1 == x_2 and y_1 == y_2 and r_1 == r_2:
        print(-1)
    elif d == r_1 ** 2 + r_2 ** 2 or d == abs(r_1 - r_2) ** 2:
        print(1)
    elif abs(r_1 - r_2) < d < r_1 + r_2 :
        print(2)
    else:
        print(0)