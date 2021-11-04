import sys

N = int(input())
num = []
for _ in range(N):
    num.append(int(sys.stdin.readline()))



def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def get_primes(m, n):
    numbers = set(range(n, 1, -1))
    prime_number = []
    for i in range(len(numbers)):
        p = list(numbers)[i]
        numbers.difference_update(set(range(p*2, n+1, p)))
        if p >= m:
            prime_number.append(p)
        if len(numbers) - 1 == i: break
    return prime_number

prime_number = sorted(get_primes(0, 10000), reverse=True)

for i in num:
    if is_prime(i // 2):
        print(i // 2, i // 2)
    else:
        for j in prime_number:
            if j < i // 2:
                small_prime = j
                big_prime = i - small_prime
                if is_prime(big_prime):
                    print(small_prime, big_prime)
                    break
        