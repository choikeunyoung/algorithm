while True:
    num = int(input())
    if num == 0:
        break
    else:
        answer = 0
        for i in range(1,num+1):
            answer += i
        print(answer)