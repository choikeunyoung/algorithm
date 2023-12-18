import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    total_list = []
    for __ in range(N):
        person_list = list(map(int, input().split()))
        total_list.append(person_list)

    total_list.sort(key=lambda x: x[0])
    answer_list = []
    answer_list.append(total_list[0][:])
    for i in total_list[1:]:
        for k in answer_list:
            if k[1] > i[1]:
                if k[0] < k[1]:
                    answer_list.append(i)
                    break
    print(answer_list)
