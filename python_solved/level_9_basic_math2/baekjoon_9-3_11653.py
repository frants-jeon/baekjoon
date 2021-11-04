def is_prime_number(n : int):
    if n <= 1:
        return False
    else:
        remainder = 0
        for i in range(1, n + 1):
            if n % i == 0:
                remainder += 1
                if remainder > 2: break
        if remainder == 2:
            return True
N = int(input())
if N != 1:
    while 1:
        if is_prime_number(N): break
        for i in range(2, N + 1):
            if N % i == 0 and is_prime_number(i):
                N = N // i
                print(i)
                break
    print(N)