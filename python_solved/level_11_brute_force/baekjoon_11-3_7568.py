##### 덩치 #####
N = int(input())
people = []
for _ in range(N):
    person = list(map(int,input().split()))
    people.append(person)

people = list(zip(*people))
kg_list = list(people[0])
cm_list = list(people[1])

rank_list = []
for i in range(N):
    target_rank = 1
    for j in range(N):
        if i == j:
            continue
        if kg_list[i] < kg_list[j] and cm_list[i] < cm_list[j]:
            target_rank += 1
    rank_list.append(target_rank)

for k in range(len(rank_list)):
    if k == len(rank_list) - 1:
        print(rank_list[k])
    else:
        print(rank_list[k], end=' ')
