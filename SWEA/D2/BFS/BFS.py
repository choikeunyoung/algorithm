# # 트리용 BFS

# def BFS(start):
#     print(start, end=" ")
#     for i in range(6):
#         if matrix[start][i] == 1:
#             queue.append(i)
#     while queue:
#         check = queue.pop(0)
#         visited[check] = True
#         for j in range(6):
#             if matrix[check][j] == 1:
#                 if not visited[j]:
#                     queue.append(j)
#         print(check, end=" ")
            

# matrix = [
#     [0, 1, 0, 0, 1, 0],
#     [0, 0, 1, 0, 0, 1],
#     [0, 0, 0, 1, 0, 0],
#     [0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0]
# ]

# queue = []
# visited = [False] * 6
# N = int(input())
# BFS(N)

# 그래프 BFS

def BFS(start):
    print(start)
    visited[start] = True
    for i in range(6):
        if matrix[start][i] == 1:
            queue.append(i)
    while queue:
        check = queue.pop(0)
        if not visited[check]:
            print(check)
        visited[check] = True
        for j in range(6):
            if matrix[check][j] == 1:
                if not visited[j]:
                    queue.append(j)
        
            

matrix = [
    [0, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0],
    [1, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1],
    [0, 0, 1, 1, 0, 0]
]

queue = []
visited = [False] * 6
N = int(input())
BFS(N)