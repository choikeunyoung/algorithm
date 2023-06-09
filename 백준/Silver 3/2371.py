N = int(input())

answer_list = []
length_list = []

for _ in range(N):
    num_list = list(map(int,input().split()))
    num_length = len(num_list)
    length_list.append(num_length)
    answer_list.append(num_list)

max_value = max(length_list)

for i in answer_list:
    if len(i) < max_value:
        middle_value = max_value - len(i)
        i[-1] = 0
        for _ in range(middle_value):
            i.append(0)
        i[-1] = -1

list_length = len(answer_list)

for j in range(max_value-1):
    cnt = 0
    check = []
    for k in range(list_length):
        if answer_list[k][j] not in check:
            check.append(answer_list[k][j])
    if len(check) == list_length:
        print(j+1)
        break