import sys

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    T = int(input())
    num_list = []
    for _ in range(T):
        num_list.append(int(input()))
    cnt = 1
    while True:
        check_list = set()
        for k in num_list:
            check_list.add(k%cnt)
        if len(check_list) == N:
            print(cnt)
            break
        cnt += 1