N = int(input())

num_list = []
no_list = []

for _ in range(N):
    call_list = list(map(int,input().split()))
    call_list[0] = str(call_list[0])
    if call_list[1] == 0 and call_list[2] == 0:
        for i in call_list[0]:
            if i not in no_list:
                no_list.append(i)
    else:
        num_list.append(call_list)

num_length = len(num_list)

for i in range(num_length):
    if i[1] == 3:
        print(1)
        break
    else:
        for j in range(3):
            if i[j] in no_list:
                pass
            else:
                for k in range(i,num_length):