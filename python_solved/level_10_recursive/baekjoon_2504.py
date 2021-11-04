S = input()
a = '('
b = ')'
c = '['
d = ']'
e = [a,b,c,d,'x']
cnt = 0
def parenthesis(s: list):
    global cnt
    if s.count(a) != s.count(b) or s.count(c) != s.count(d) or cnt > 500:
        print(0)
        return
    if len(s) == 1:
        print(s[0])
        return
    for i in range(len(s) - 1):
        if s[i] == a and s[i + 1] == b:
            s[i] = 'x'
            s[i + 1] = 2
    for j in range(len(s) - 1):
        if s[j] == c and s[j + 1] == d:
            s[j] = 'x'
            s[j + 1] = 3
    while s.count('x') != 0:
        s.pop(s.index('x'))

    for k in range(1,len(s) - 1):
        if s[k - 1] not in e and s[k] not in e:
            s[k] = s[k - 1] + s[k]
            s[k - 1] = 'x'
        if s[k + 1] not in e and s[k] not in e:
            s[k + 1] = s[k + 1] + s[k]
            s[k] = 'x'
    while s.count('x') != 0:
        s.pop(s.index('x'))

    for k in range(1, len(s) - 1):
        if s[k - 1] == a and s[k + 1] == b:
            s[k - 1] = 'x'
            s[k] = s[k] * 2
            s[k + 1] = 'x'
        if s[k - 1] == c and s[k + 1] == d:
            s[k - 1] = 'x'
            s[k] = s[k] * 3
            s[k + 1] = 'x'
    while s.count('x') != 0:
        s.pop(s.index('x'))
    if len(s) == 2:
        s[0] = s[0] + s[1]
        s.pop()
    cnt += 1
    parenthesis(s)


S = list(S)
parenthesis(S)