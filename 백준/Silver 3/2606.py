n = int(input())
m = int(input())
computers = [[] for _ in range(n+1)]

for __ in range(m):
    v1, v2 = map(int,input().split())
    computers[v1].append(v2)
    computers[v2].append(v1)

stack = list(computers[1])
visited = [False] * (n+1)
while stack:
    cur = stack.pop()
    for j in computers[cur]:
        if visited[j] == False:
            visited[j] = True
            stack.append(j)
print(visited.count(True)-1)