# #틀림
# N = int(input())
# lcm = 15 #최소공배수(Least Common Multiple)
# dic = {3: 1, 5: 1, 6: 2, 8: 2, 9: 3, 10: 2, 11: 3, 12: 4, 13: 3, 14: 4} 
# small = 0
# while 1:
#     if N == 4 or N == 7:
#         small = -1
#         break
#     if N < lcm:
#         small += dic[N]
#         break
#     elif N % lcm == 0:
#         small += N // lcm * 3
#         break
#     elif N - 3 in dic:
#         small += 1 + dic[N - 3]
#         break
#     elif N - 5 in dic:
#         small += 1 + dic[N - 5]
#         break
#     else:
#         N -= lcm
#         if N in dic:
#             small += 3 + dic[N]
#         else:
#             small += 3
#         if N in dic: break
# print(small)

N = int(input())
def sugar_small(n):
    dic = {3: 1, 5: 1, 6: 2, 8: 2, 9: 3, 10: 2, 11: 3, 12: 4, 13: 3, 14: 4, 15: 3, 16: 4, 17: 5} 
    result = 0
    if n < 18:
        if n in dic:
            result += dic[n]
        elif not N in dic:
            result -= 1
    elif n % 15 == 0:
        result += n // 5
    elif n - 15 < 8:
        result += 1 + sugar_small(n - 5)
    else:
        result += 3 + sugar_small(n - 15)
    return result
print(sugar_small(N))