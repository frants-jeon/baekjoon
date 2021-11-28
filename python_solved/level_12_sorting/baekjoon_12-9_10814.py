##### 나이순 정렬 #####
import sys
N = int(sys.stdin.readline())
people = []
for i in range(N):
    temp = list(map(str,sys.stdin.readline().strip('\n').split()))
    age = int(temp[0])
    name = temp[1]
    person = (i, age, name)
    people.append(person)


people.sort(key=lambda x: (x[1], x[0]))
for person in people:
    print(person[1], person[2])

# print(*sorted([*open(0)][1:],key=lambda a:int(a.split()[0])),sep='')
# print(''.join(sorted([*open(0)][1:],key=lambda x:int(x.split()[0]))))
