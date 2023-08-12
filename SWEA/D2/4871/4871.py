T = int(input())

for tc in range(1, T+1):
    V, E = map(int,input().split())
    node_list = [[] for _ in range(V)]
    flag = 0
    for _ in range(E):
        nodes = list(map(int,input().split()))
        node_list[nodes[0] - 1].append(nodes[1] - 1)
    
    for i in node_list:
        i.sort(reverse=True)
        
    end_point = list(map(int,input().split()))
    visited = [False]*V
    stack = node_list[end_point[0] - 1]
    visited[end_point[0] - 1] = True
    while stack:
        check = stack.pop()
        if check == end_point[1]-1:
            flag = 1
            break
        else:
            if not visited[check]:  
                stack.extend(node_list[check])
                visited[check] = True
    
    if flag == 1:
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")