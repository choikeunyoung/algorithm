T = int(input())

def selection(num):
    notUser = [graph[num]]
    

for tc in range(1, T+1):
    N = int(input())
    way_list = list(map(int,input().split()))
    
    graph = [[] for _ in range(N)]
    
    for i in range(N):
        if i == 0:
            graph[i].append(N-1)
            graph[i].append(i+1)
        else:
            graph[i].append(i-1)
            graph[i].append(i+1)