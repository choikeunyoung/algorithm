def answer(num):
    cnt_list = [0,0,1,1] + [0]*(num-3)
    num_list = ["0","1","2","3"] + [""]*(num-3)
    for i in range(4, num+1):
        if i % 2 == 0 and i % 3 == 0:
            if cnt_list[i // 2] + 1 > cnt_list[i // 3] + 1:
                cnt_list[i] = cnt_list[i // 3] + 1
                num_list[i] = num_list[i // 3] + "3"
            else:
                cnt_list[i] = cnt_list[i // 2] + 1
                num_list[i] = num_list[i // 2] + "2"
        else:
            if i % 2 == 0:
                if cnt_list[i // 2] + 1 > cnt_list[i-1] + 1:
                    cnt_list[i] = cnt_list[i - 1] + 1
                    num_list[i] = num_list[i - 1] + "-"
                else:
                    cnt_list[i] = cnt_list[i // 2] + 1
                    num_list[i] = num_list[i // 2] + "2"
            elif i % 3 == 0:
                if cnt_list[i // 3] + 1 > cnt_list[i-1] + 1:
                    cnt_list[i] = cnt_list[i - 1] + 1
                    num_list[i] = num_list[i - 1] + "-"
                else:
                    cnt_list[i] = cnt_list[i // 3] + 1
                    num_list[i] = num_list[i // 3] + "3"
            else:
                cnt_list[i] = cnt_list[i - 1] + 1
                num_list[i] = num_list[i - 1] + "-"
    return cnt_list[num],num_list[num]

N = int(input())
if N < 4:
    if N == 2:
        print(1)
        print(2, 1)
    elif N == 3:
        print(1)
        print(3, 1)
    else:
        print(0)
        print(1)
else:
    ans_list = answer(N)
    print(ans_list[0])
    for i in ans_list[-1][::-1]:
        print(N, end=" ")
        if i == "-":
            N -= 1
        elif i == "2":
            N //= 2
        else:
            N //= 3
    print(1)