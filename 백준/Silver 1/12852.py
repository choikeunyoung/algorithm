def answer(num):
    num_list = ["0", "1", "1 2", "1 3"] + ["1"] * (10**6-2)
    for i in range(4,10**6+1):
        if i % 2 == 0 and i % 3 == 0:
            if len(num_list[i // 2]) > len(num_list[i // 3]):
                num_list[i] = num_list[i // 3] + " " + str(i)
            elif len(num_list[i // 2]) < len(num_list[i // 3]):
                num_list[i] = num_list[i // 2] + " " + str(i)
        else:
            if i % 2 == 0:
                if len(num_list[i // 2]) > len(num_list[i-1]):
                    num_list[i] = num_list[i - 1] + " " + str(i)
                else:
                    num_list[i] = num_list[i // 2] + " " + str(i)
            elif i % 3 == 0:
                if len(num_list[i // 3]) > len(num_list[i-1]):
                    num_list[i] = num_list[i - 1] + " " + str(i)
                else:
                    num_list[i] = num_list[i // 3] + " " + str(i)
            else:
                num_list[i] = num_list[i - 1] + " " + str(i)
    return num_list[num]

N = int(input())
ans = answer(N)
ans_list = list(ans.split())
print(len(ans_list)-1)
for i in ans_list[::-1]:
    print(i, end=" ")