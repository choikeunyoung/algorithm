import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for tc in range(T):
    N, search = map(int, input().split())
    priority_list = list(map(int, input().split()))
    for i, v in enumerate(priority_list):
        priority_list[i] = (v, i)
    priority_list = deque(priority_list)
    max_value = max(priority_list)[0]
    cnt = 1
    while True:
        if max_value == priority_list[0][0]:
            if priority_list.popleft()[-1] == search:
                print(cnt)
                break
            else:
                max_value = max(priority_list)[0]
            cnt += 1
        else:
            priority_list.rotate(-1)
