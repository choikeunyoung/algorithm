from collections import deque
N = int(input())
crain_list = list(map(int,input().split()))

M = int(input())
box_list = list(map(int,input().split()))

crain_list.sort(reverse=True)
box_list.sort(reverse=True)
box_list = deque(box_list)
box_dict = {}
for i in box_list:
    if i in box_dict:
        box_dict[i] += 1
    else:
        box_dict[i] = 1
if box_list[0] > crain_list[0]:
    print(-1)
else:
    cnt = 1
    while True:
        for i in range(N):
            flag = 0
            if not box_list:
                print(cnt)
                exit()
            check = box_list.popleft()
            if check > crain_list[i]:
                check_cnt = 0
                max_length = len(box_list) + 1
                while check > crain_list[i]:
                    if check_cnt == max_length:
                        box_list.append(check)
                        break
                    box_list.append(check)
                    check = box_list.popleft()
                    check_cnt += 1
                    if check == crain_list[i]:
                        flag = 1
                        box_dict[check] -= 1
                        break
        if not box_list:
            print(cnt)
            exit()
        for v in range(box_dict[check]):
            check = box_list.popleft()
            box_list.append(check)
        cnt += 1

