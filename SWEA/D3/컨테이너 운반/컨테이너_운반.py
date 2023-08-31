T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())
    container_list = list(map(int,input().split()))
    truck_list = list(map(int,input().split()))
    container_list.sort()
    truck_list.sort()
    max_weight = 0
    while truck_list:
        if truck_list and container_list:
            check = container_list.pop()
            if truck_list[-1] >= check:
                truck_list.pop()
                max_weight += check
        else:
            break
    if max_weight == 0:
        print(f"#{tc} 0")
    else:
        print(f"#{tc} {max_weight}")