N = int(input())
num_list = list(map(int,input().split()))
check_list = list(num_list)
list_length = len(num_list)
index = 0
while check_list:
    print(num_list.index(check_list[index])+1, end=" ")
    check = check_list.pop(index) + index
    list_length -= 1
    if check > 0:
        if check > list_length:
            check -= list_length
    elif check < 0:
        check += list_length
    print(check, index)
    index = check -1