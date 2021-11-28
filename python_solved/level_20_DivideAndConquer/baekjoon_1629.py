##### 곱셈 #####
from sys import stdin

A, B, C = map(int,stdin.readline().split())
def my_pow(base, exp):
    if exp == 1:
        return base
    if exp % 2 == 0:
        return (my_pow(base, exp // 2) ** 2) % C
    else:
        return ((my_pow(base, exp // 2) ** 2) * base) % C
print(my_pow(A, B))
print(pow(A,B,C))