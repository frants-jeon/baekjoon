N, R, C = map(int,input().split())

def move_z(n, r, c):
    if n == 1:
        return 0
    
    if r < n // 2 and c < n // 2:
        return move_z(n // 2, r, c)
    elif r < n // 2 and c >= n // 2:
        return move_z(n // 2, r, c - n // 2) + n ** 2 // 4
    elif r >= n // 2 and c < n // 2:
        return move_z(n // 2, r - n // 2, c) + n ** 2 // 2
    else:
        return move_z(n // 2, r - n // 2, c - n // 2) + n ** 2 * 3 // 4 

print(move_z(2**N, R, C))