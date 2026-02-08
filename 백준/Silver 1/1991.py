import sys

input = sys.stdin.readline

N = int(input())

tree = {}

for _ in range(N):
    root, left, right = input().split()
    tree[root] = (left, right)


def pre(node):
    if node == ".":
        return
    print(node, end="")
    pre(tree[node][0])
    pre(tree[node][1])


def inorder(node):
    if node == ".":
        return
    inorder(tree[node][0])
    print(node, end="")
    inorder(tree[node][1])


def post(node):
    if node == ".":
        return
    post(tree[node][0])
    post(tree[node][1])
    print(node, end="")


pre("A")
print()
inorder("A")
print()
post("A")
