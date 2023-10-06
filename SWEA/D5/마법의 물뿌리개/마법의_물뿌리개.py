def DFS(start):
    

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    tree_list = list(map(int,input().split()))
    max_tree = max(tree_list)
    total = 0
    day = 0
    one_cnt = 0
    two_cnt = 0
    for i in range(N):
        tree_list[i] = max_tree - tree_list[i]
        total += tree_list[i]
    if total == 0:
        print(f"#{tc} {day}")
    else:
        for i in range(N):
            if tree_list[i] != 0:
                day += (tree_list[i]//3)*2
                tree_list[i] = tree_list[i] - (tree_list[i]//3)*3
        total = sum(tree_list)
        if total%3 == 0:
            day += (total//3)*2
        else:
            if one_cnt == 0 and two_cnt != 0:
                if two_cnt%3 == 1:
                    day += 
        print(f"#{tc} {day}")