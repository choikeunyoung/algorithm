def DFS(graph, N, V):
    visited = [False] 
    w
    

def BFS(graph, N, V):
    

N, M, V = map(int,input().split())

graph_dict = {}

for i in range(1,N+1):
    nums = list(map(int,input().split()))
    if nums[0] in graph_dict:
        graph_dict.update({nums[0]:nums[1]})
    else:
        graph_dict[nums[0]] = nums[1]
print(graph_dict)