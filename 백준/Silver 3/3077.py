N = int(input())

answer_list = list(map(str,input().split()))
check_list = list(map(str,input().split()))
cnt = 0


for i in range(N):
    first_answer = check_list[i]
    for j in range(i+1,N):
        second_answer = check_list[j]
        flag = 0
        for k in range(N):
            if answer_list[k] == first_answer:
                first_index = k
                flag += 1
            if answer_list[k] == second_answer:
                second_index = k
                flag += 1
            if flag == 2:
                break
        if first_index < second_index:
            cnt += 1

total = (N*(N-1))//2

print(f"{cnt}/{total}")