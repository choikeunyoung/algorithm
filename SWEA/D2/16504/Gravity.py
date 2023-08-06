# import sys

# sys.stdin = open("./input.txt",'r')

# T = int(sys.stdin.readline())
# 박스의 칸수를 오른쪽으로 옮기는 것으로 해결
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    box_list = list(map(int,input().split()))
    max_cnt = 0
    for i in range(N):
        cnt = 0
        for j in range(i,N):
            if box_list[i] > box_list[j]:
                cnt += 1
            elif box_list[i] < box_list[j]:
                break
        if max_cnt < cnt:
            max_cnt = cnt
    print(f"#{tc} {max_cnt}")