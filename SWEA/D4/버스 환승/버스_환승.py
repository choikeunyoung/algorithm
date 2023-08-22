from collections import deque

def BFS(start):
    queue = deque(start)

    
    
M, N = map(int,input().split())

K = int(input())

bus_list = [[] for _ in range(K+1)]

bus_dict = {}

for _ in range(K):
    buses = list(map(int,input().split()))
    for i in range(min(buses[1],buses[3]), max(buses[1],buses[3])+1):
        for j in range(min(buses[2], buses[4]), max(buses[2],buses[4])+1):
            if buses[0] in bus_dict.keys():
                bus_dict[buses[0]].append((i,j))
            else:
                bus_dict[buses[0]] = [(i,j)]

graph = [ [] for _ in range(N+1)]


for j in range(1,N+1):
    flag = 0 
    for k in bus_dict[j]:
        for l in range(j+1,N+1):
            print(k, l, bus_dict[l])
            if k in bus_dict[l]:
                graph[j].append(l)
                graph[l].append(j)
                flag = 1
                break
        if flag == 1:
            break
print(graph)

pos = list(map(int,input().split()))

for i in range(1,N+1):
    if (pos[0],pos[1]) in bus_dict[i]:
        
        break