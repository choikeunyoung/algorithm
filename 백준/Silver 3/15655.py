def DFS(num):
    if num == M:
        if sorted(ans) not in answer:
            answer.append(ans[:])
        return
    else:
        for i in range(N):
            if num_list[i] not in ans:
                ans.append(num_list[i])
                DFS(num+1)
                ans.pop()


N, M = map(int,input().split())
num_list = list(map(int,input().split()))
num_list.sort()
ans = []
answer = []

DFS(0)
for i in answer:
    print(*i)