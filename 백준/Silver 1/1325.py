import sys
from collections import deque

input = sys.stdin.readline

def BFS(start):
    cnt = 1
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        check = queue.popleft()
        if graph[check]:
            for k in graph[check]:
                if not visited[k]:
                    visited[k] = True
                    queue.append(k)
                    cnt += 1
    return cnt

N, M = map(int,input().split())
graph = [set() for _ in range(N+1)]
ans_list = ""
for _ in range(M):
    A, B = map(int,input().split())
    graph[B].add(A)

max_value = 0

for i in range(1,N+1):
    visited = [False] * (N+1)
    answer_cnt = BFS(i)
    if answer_cnt > max_value:
        max_value = answer_cnt
        ans_list = ""
        ans_list += str(i)+" "
    elif answer_cnt == max_value:
        ans_list += str(i)+" "

print(ans_list.strip())