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
    print(total)
    if total == 0:
        print(f"#{tc} {day}")
    else:
        while total > 0:
            day += 1
            if day % 2 == 0:
                for k in range(N):
                    if tree_list[k] != 0 and tree_list[k]%2 == 0:
                        tree_list[k] -= 2
                        total -= 2
                        break
            else:
                for k in range(N):
                    if tree_list[k] != 0 and tree_list[k]%2 == 1:
                        tree_list[k] -= 1
                        total -= 1
                        break
        print(f"#{tc} {day}")
