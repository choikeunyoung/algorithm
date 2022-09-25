T = int(input())
for i in range(T):
    num_list = list(map(int,input().split()))
    nums = 0
    cnt = 0
    num_index = 0
    final_list = []
    while len(num_list) >= 8:
        if nums < num_list[cnt]:
            nums = num_list[cnt]
            num_index = cnt
        cnt += 1
        if cnt == len(num_list):
            nums = 0
            final_list.append(num_list.pop(num_index))
            cnt = 0
        
    print(final_list[-1])
