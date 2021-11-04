# def lotto_print(count_num, num_list : list, position_index, usable_num_count):
#     using = [n for n in range(position_index, count_num - usable_num_count + 1)]
#     old = 
#     if position_index == 5:
#         while len(num_list) > 5:
#             l.append(num_list[0:6])
#             num_list.pop(position_index)
#         return
#     else:
#         lotto_print(count_num, num_list, position_index + 1, usable_num_count - 1)
#         num_list.pop(position_index)
#         lotto_print(count_num, num_list, position_index + 1, usable_num_count - 1)




# while 1:
#     S = list(map(int,input().split()))
#     k = S.pop(0)
#     l = []
#     lotto_print(k, S, 0, 6)
#     print(l)
#     if k == 0: break

import sys
input = sys.stdin.readline
 
 
def backTracking(index, S, visit, printList):
    if len(printList) == 6:
        print(*printList)
        return
 
    for i in range(index, len(S)):
        if not visit[i]:
            visit[i] = True
            printList.append(S[i])
            backTracking(i, S, visit, printList)
 
            printList.pop()
            visit[i] = False

 
while True:
    case = list(map(int, input().split()))
    k = case[0]
    if k == 0:
        exit()
 
    S = case[1:]
 
    printList = []
    
    visit = [False] * len(S)
    backTracking(0, S, visit, printList)
    print()