N, Q = map(int,input().split())

ans_list = []
graph_list = [ [] for _ in range(N) ]
for i in range(N):
    pos = list(map(int,input().split()))
    pos.append(i)
    ans_list.append(pos)

ans_list.sort()

for i in range(N):
    for j in range(N):
        if j != i:
            if (ans_list[i][0] <= ans_list[j][0] <= ans_list[i][1]):
                    graph_list[ans_list[j][-1]].append(ans_list[i][-1])
                    graph_list[ans_list[i][-1]].append(ans_list[j][-1])

for _ in range(Q):
    start, end = map(int,input().split())
    stack = graph_list[start-1]
    visited = [False] * N
    while stack:
        check = stack.pop()
        next = graph_list[check]
        if end-1 in next:
            print(1)
            break
        if not visited[check]:
            visited[check] = True
            if next:
                stack.extend(next)

    else:
        print(0)