import sys

def get_primes(n : int):
    numbers = set(range(n, 1, -1))
    prime_number = []
    while numbers:
        p = numbers.pop()
        numbers.difference_update(set(range(p * 2, n + 1, p)))
        prime_number.append(p)
        
    return prime_number
prime_number = get_primes(123456 * 2)

while 1:
    n = int(sys.stdin.readline())
    cnt = 0 # prime number count
    if n == 0: break
    for i in prime_number:
        if n < i <= 2*n:
            cnt += 1
    print(cnt)
