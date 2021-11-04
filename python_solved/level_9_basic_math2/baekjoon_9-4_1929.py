
# def get_primes(m, n):
#     numbers = set(range(n, 1, -1))
#     prime_number = []
#     for i in range(len(numbers)):
#         p = list(numbers)[i]
#         numbers.difference_update(set(range(p*2, n+1, p)))
#         if p >= m:
#             prime_number.append(p)
#         if len(numbers) - 1 == i: break
#     return prime_number
# for i in get_primes(M, N):
#     print(i)

# prime number 빠르게 찾는 법 서치
M, N = map(int,input().split())
def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
for x in range(M, N + 1):
    if is_prime(x):
        print(x)