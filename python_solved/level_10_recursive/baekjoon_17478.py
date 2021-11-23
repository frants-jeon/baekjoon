N = int(input())


def recursive(n):
    print(n)
    if n == 0:
        print()
        return
    recursive(n - 1)
    print(n)

print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')
recursive(N)
print('라고 답변하였지.')