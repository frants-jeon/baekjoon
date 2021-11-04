prime_number = [2]
max_number = 10000
for i in range(3,max_number):
    remainder = 0
    for j in prime_number:
        if i % j == 0:
            remainder += 1
    if remainder == 0:
        prime_number.append(i)
M = int(input())
N = int(input())
M_to_N_prime_number = [x for x in prime_number if M <= x <= N]
if sum(M_to_N_prime_number) != 0:
    print(sum(M_to_N_prime_number))
    print(min(M_to_N_prime_number))
else: print(-1)