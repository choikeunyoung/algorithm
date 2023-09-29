def DFS(num):
    if num == M:
        answer.add(ans[:])
        return
    else:
        for i in range(N):
            ans.append(num_list[i])
            DFS(num+1)
            ans.pop()

N, M = map(int,input().split())
num_list = list(map(int,input().split()))
num_list.sort()
ans = ()
answer = set()
DFS(0)

for i in answer:
    print(*i)