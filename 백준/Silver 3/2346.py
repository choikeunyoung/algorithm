N = int(input())
flag = N
num_list = list(map(int,input().split()))
check_list = list(num_list)
list_length = len(num_list)
index = 0
while True:
    check = check_list[index]
    print(num_list)
    print(num_list.index(check)+1, end=" ")
    num_list[index] = 0
    check_list[index] = 0
    index += check
    flag -= 1
    if flag == 0:
        break
    if index >= list_length:
        index = index - (index//list_length)*list_length
    elif index < 0:
        index = index + (abs(index)//list_length)*list_length
    if check_list[index] == 0:
        cnt = 0
        while True:
            if check > 0:
                index += 1
                if index >= list_length:
                    index -= list_length
            elif check < 0:
                index -= 1
                if abs(index) >= list_length:
                    index += list_length
            if check_list[index] != 0 or cnt == N:
                break
            cnt += 1