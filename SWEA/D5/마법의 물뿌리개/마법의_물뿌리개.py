T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    tree_list = list(map(int,input().split()))
    max_tree = max(tree_list)
    total = 0
    day = 0
    for i in range(N):
        tree_list[i] = max_tree - tree_list[i]
        total += tree_list[i]
    
    if total == 0:
        print(f"#{tc} {day}")
    else:
        for i in range(N):
            if tree_list[i]//4 > 0 and tree_list[i] != 0:
                day += (tree_list[i]//4*3)
                tree_list[i] = tree_list[i] - (tree_list[i]//4)*4
                if tree_list[i]%4 == 2 or tree_list[i] == 3:
                    day += 2
                elif tree_list[i]%2 == 1:
                    day += 1
                else:
                    day += 3
            elif tree_list[i]//4 == 0 and tree_list[i] != 0:
                if tree_list[i]%4 == 2 or tree_list[i] == 3:
                    day += 2
                elif tree_list[i]%2 == 1:
                    day += 1
                else:
                    day += 3
        print(f"#{tc} {day}")