def DFS(num):
    if len(ans) == M:
        print(*ans)
        return
    else:
        for i in range(num, N):
            ans.append(num_list[i])
            DFS(i)
            ans.pop()


N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()
ans = []
DFS(0)
