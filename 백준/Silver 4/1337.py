import sys

input = sys.stdin.readline

N = int(input())

num_list = []
check_list = []

for _ in range(N):
    number = int(input())
    base_list = [number]
    for i in range(1,5):
        base_list.append(number+i)
    check_list.append(base_list)
    num_list.append(number)

num_list.sort()
answer_list = []
print(check_list,num_list)

for i in check_list:
    cnt = 0
    for j in num_list:
        if j in i:
            cnt += 1
    answer_list.append(5-cnt)
print(answer_list)  