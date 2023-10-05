from collections import deque


def BFS():
    q = deque(start)
    visited[start] = 1
    global ans
    while q:
        check = q.popleft()
        if end % num_list[check] == 0:
            print(visited[check])
            break
        else:
            for 

N = int(input())
num_list = list(map(int,input().split()))
visited = [0] * N
start, end = map(int,input().split())
start -= 1
end -= 1

BFS()