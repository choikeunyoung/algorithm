def answer(num):
    num_list = [0,0,1,1] + [0]*(10**6-2)
    for i in range(4, 10**6+1):
        if i % 3 == 0 and i % 2 == 0:
            num_list[i] = min(num_list[i // 3]+1,num_list[i // 2]+1)
        else:
            if i % 3 == 0:
                num_list[i] = min(num_list[i // 3]+1,num_list[i-1] + 1)
            elif i % 2 == 0:
                num_list[i] = min(num_list[i // 2]+1,num_list[i-1] + 1)
            else:
                num_list[i] = (num_list[i-1] + 1)
    return num_list[num]
N = int(input())

print(answer(N))