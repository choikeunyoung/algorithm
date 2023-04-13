answer = input()

cnt = 1
index = 0
flag = 0
while True:
    if cnt >= 10:
        for j in str(cnt):
            if int(j) == int(answer[index]):
                index += 1
            if index == len(answer):
                flag = 1
                break
    else:
        if cnt == int(answer[index]):
            index += 1
    if flag == 1:
        print(cnt)
        break
    else:
        if index == len(answer):
            print(cnt)
            break
    cnt += 1