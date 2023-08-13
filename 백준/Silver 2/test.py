def BFS(graph):
    visited = [False] * len(graph)
    visited[0] = True
    stack = graph[0]
    answer = [1]
    while stack:
        next_step = stack.pop(0)-1
        if not visited[next_step]:
            stack.extend(graph[next_step])
            visited[next_step] = True
            answer.append(next_step+1)
    return answer

graph = [
    [2, 3, 4],
    [1, 5, 6, 7],
    [1],
    [1, 11],
    [2],
    [2, 9],
    [2, 10],
    [],
    [6],
    [7],
    [4],
]

print(BFS(graph))