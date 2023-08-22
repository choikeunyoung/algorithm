T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int,input().split()))
    last = 0
    tree = [[] for _ in range(N+1)]
    for i in range(N):
        last += 1
        tree[last] = num_list[i]
    c = last
    p = last//2
    
    while p > 0 and tree[p] > tree[c]:
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c//2
    print(tree)