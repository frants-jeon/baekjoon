N = int(input())
node = []
for _ in range(N):
    n = list(map(str,input().split()))
    node.append(n)



# 전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
def preorder_traversal(a):
    print(a, end='')
    for i in node:
        if i[0] == a: break
    if i[1] != '.':
        preorder_traversal(i[1])
    if i[2] != '.':
        preorder_traversal(i[2])

# 중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
def inorder_traversal(a):
    for j in node:
        if j[0] == a: break
    if j[1] != '.':
        inorder_traversal(j[1])
    print(a,end='')
    if j[2] != '.':
        inorder_traversal(j[2])


# 후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)
def postorder_traversal(a):
    for k in node:
        if k[0] == a: break
    if k[1] != '.':
        postorder_traversal(k[1])
    if k[2] != '.':
        postorder_traversal(k[2])
    print(a,end='')


preorder_traversal('A')
print()
inorder_traversal('A')
print()
postorder_traversal('A')