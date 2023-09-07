def checking(num):
    global check
    global cnt
    global ans
    if len(num) == 1:
        if int(check) > int(num[0]):
            cnt += 1
            ans = 1
        else:
            ans = 0
        return
    if check == "":
        check = num[0]
        checking(num[1:])
    else:
        if int(num[0]) < int(check):
            check = num[0]
            checking(num[1:])
        else:
            ans = 0
            return

N = int(input())

cnt = -1
number = 0
limit_check = 1
ten_check = 1
while cnt <= 10**6:
    if number < 10:
        cnt += 1
    else:
        check = ""
        ans = 0
        print(number)
        checking(str(number))
        print(ans)
        if ans == 0:
            ten_check += 1
            if ten_check == 10:
                limit_check += 1
                ten_check = 1
            number = ten_check * (10**limit_check)
        else:
            number += 1
    print(cnt,number)
    if cnt == N:
        print(number-1)
        break
    if cnt < 10:
        number += 1
    if limit_check > 9:
        print(-1)
        break