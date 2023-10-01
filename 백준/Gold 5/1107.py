def make_perm(num):
    global ans_cnt
    if ans_cnt == 2:
        return
    if num == N_length:
        checking = int("".join(ans))
        if checking >= N:
            answer.append(checking)
            ans_cnt += 1
        else:
            if answer:
                ans_cnt -= 1
                answer.pop()
            ans_cnt += 1
            answer.append(checking)
        return
    else:
        for i in range(check_length):
            ans.append(check_num[i])
            make_perm(num+1)
            ans.pop()


N = input()
N_length = len(N)
N = int(N)
cnt = int(input())
if cnt != 0:
    num_list = list(map(int,input().split()))
current = 100

if current == N:
    print(0)
else:
    if cnt == 0:
        print(min(abs(N-current),N_length))
    else:
        check_num = []
        ans_cnt = 0
        for i in range(10):
            if i not in num_list:
                check_num.append(str(i))
        check_length = len(check_num)
        ans = []
        answer = []
        if check_num:
            make_perm(0)
            min_value = 10**9
            for j in answer:
                number = abs(N-j)
                if number < min_value:
                    min_value = number
            min_value += N_length
            number = ""
            for j in range(N_length-1):
                number += check_num[-1]
            if number != "":
                number = int(number)
                if N - number + N_length-1 < min_value:
                    min_value = N - number + N_length-1
            number = ""
            if check_num[0] == "0":
                if len(check_num) > 1 and check_num[0] == "0":
                    number += check_num[1]
                for j in range(N_length):
                    number += check_num[0]
            else:
                for j in range(N_length+1):
                    number += check_num[0]
            if number != "":
                number = int(number)
                if number == 0:
                    if abs(number - N) + 1 < min_value:
                        min_value = abs(number - N) + 1
                else:
                    if abs(number - N) + N_length + 1 < min_value:
                        min_value = abs(number - N) + N_length + 1
            if min_value > abs(N-current):
                min_value = abs(N-current)
            print(min_value)
        else:
            print(min(abs(N-current),abs(current-N)))