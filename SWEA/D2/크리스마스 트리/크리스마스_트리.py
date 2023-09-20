def inorder(start):
    stack = tree_dict[start][:]
    if stack[0] != -1:
        inorder(stack[0])
    print(start, end=" ")
    if stack[1] != -1:
        inorder(stack[1])
        
        
def preorder(start):
    stack = tree_dict[start][:]
    print(start, end=" ")
    while stack:
        check = stack.pop(0)
        if check != -1:
            preorder(check)
    
    
def postorder(start):
    stack = tree_dict[start][:]
    while stack:
        check = stack.pop(0)
        if check != -1:
            postorder(check)
    print(start, end=" ")

N = int(input())

tree_dict = {}

for _ in range(N):
    start, left, right = map(int,input().split())
    tree_dict[start] = [left,right]
    
    
inorder(1)
print()
preorder(1)
print()
postorder(1)