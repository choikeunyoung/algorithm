def all_number(num):
    if num == 0:
        print(*answer)
    else:
        for i in range(1,7):
            answer.append(i)
            all_number(num-1)
            answer.pop()


def all_number_2(num):
    if num == 0:
        print(*answer)
    else:
        for i in range(1,7):
                if answer:
                    if i >= answer[-1]:
                        answer.append(i)
                        all_number_2(num-1)
                        answer.pop()
                else:
                    answer.append(i)
                    all_number_2(num-1)
                    answer.pop()


def all_number_3(num):
    if num == 0:
        print(*answer)
    else:
        for i in range(1,7):
            if i in answer:
                continue
            answer.append(i)
            all_number_3(num-1)
            answer.pop()

N,M = map(int,input().split())

answer = []

if M == 1:
    all_number(N)
elif M == 2:
    all_number_2(N)
elif M == 3:
    visited = [False]*7
    path = []
    all_number_3(N)