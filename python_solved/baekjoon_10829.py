N = int(input())
total = 0
def banary(n) :
    global total
    t = 0
    if n > 3:
        while 1:
            t += 1
            if 2 ** t <= n < 2 ** (t + 1): break 
    elif n == 2 or n == 3:
        t += 1
    n -= 2 ** t
    total += 10 ** t
    if n >= 1:
        banary(n)

banary(N)
print(total)