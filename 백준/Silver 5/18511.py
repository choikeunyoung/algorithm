import sys

sys.setrecursionlimit(10000)


def recur():
    global K
    global max_value
    global check_num
    if check_num > N:
        return
    else:
        if max_value < check_num:
            max_value = check_num
    for i in num_list:
        if check_num == 0:
            check_num = i
            recur()
            check_num = 0
        else:
            check_num = check_num * 10 + i
            recur()
            check_num //= 10


N, K = map(int, input().split())
num_list = list(map(int, input().split()))
max_value = 0
check_num = 0
recur()
print(max_value)
