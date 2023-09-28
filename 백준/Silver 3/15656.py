def DFS(num):
    if num == M:
        print(*ans)
        return
    else:
        for i in range(N):
            ans.append(num_list[i])
            DFS(num+1)
            ans.pop()

N, M = map(int,input().split())
num_list = list(map(int,input().split()))
num_list.sort()
ans = []
DFS(0)