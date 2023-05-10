def preorder(n):
    if n != ".":
        pre.append(n)
        preorder(tree[n][0])
        preorder(tree[n][1])
    return pre

def inorder(n):
    if n != ".":
        inorder(tree[n][0])
        inn.append(n)
        inorder(tree[n][1])
    return inn

def postorder(n):
    if n != ".":
        postorder(tree[n][0])
        postorder(tree[n][1])
        post.append(n)
    return post

N = int(input())
tree = {}
pre = []
inn = []
post = []
for n in range(N):
    a, ch1, ch2 = input().split()
    tree[a] = (ch1, ch2)
# print(tree)

preorder('A')
for i in range(len(pre)):
    print(pre[i], end='')
print()

inorder('A')
for i in range(len(inn)):
    print(inn[i], end='')
print()

postorder('A')
for i in range(len(post)):
    print(post[i], end='')
print()