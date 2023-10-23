N = int(input())
crain_list = list(map(int,input().split()))

M = int(input())
box_list = list(map(int,input().split()))

crain_list.sort(reverse=True)
box_list.sort(reverse=True)
visited = [False] * M
if crain_list[0] < box_list[0]:
    print(-1)
else:
    cnt = 1
    check = M
    for _ in range(M):
        index = 0
        for i in range(M):
            if not visited[i]:
                if crain_list[index] >= box_list[i]:
                    index += 1
                    visited[i] = True
                    check -= 1
            if index == N:
                break
        if check == 0:
            break
        cnt += 1
    print(cnt)