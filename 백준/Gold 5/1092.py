N = int(input())
crain_list = list(map(int,input().split()))

M = int(input())
box_list = list(map(int,input().split()))

crain_list.sort(reverse=True)
box_list.sort(reverse=True)

if box_list[0] > crain_list[0]:
    print(-1)
else:
    current = 0
    index = 0
    cnt = 1
    while current <= M-1:
        print(box_list[current], crain_list[index], cnt)
        if box_list[current] <= crain_list[index]:
            current += 1
        
        index += 1
        if index == N:
            index = 0
            cnt += 1
    print(cnt)