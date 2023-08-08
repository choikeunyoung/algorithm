T = int(input())
max_len = 0
final_num = []
for i in range(1,T+1):
    num_list = [T]
    num_list.append(i)
    x = 0
    x = T
    j = 0
    j = i
    while True:
        c = x-j
        if c < 0:
            break
        else:
            num_list.append(c)
            x = j
            j = c 
    if len(num_list) > max_len:
        max_len = len(num_list)
        final_num = list(num_list)
print(max_len)
for k in final_num:
    print(k, end=' ')