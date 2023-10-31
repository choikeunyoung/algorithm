from collections import deque


def BFS():
    q = deque([start])
    visited[start] = 1
    while q:
        check = q.popleft()
        distance = end - check
        if distance % num_list[check] == 0:
            print(visited[check])
            return
        r_check = check
        l_check = check
        while N-1 >= r_check:
            if r_check != check and visited[r_check] == 0:
                q.append(r_check)
                visited[r_check] = visited[check] + 1
            r_check += num_list[check]
        
        while 0 <= l_check:
            if l_check != check and visited[l_check] == 0:
                q.append(l_check)
                visited[l_check] = visited[check] + 1
            l_check -= num_list[check]
    else:
        print(-1)


N = int(input())
num_list = list(map(int,input().split()))
visited = [0] * N
start, end = map(int,input().split())
start -= 1
end -= 1

BFS()