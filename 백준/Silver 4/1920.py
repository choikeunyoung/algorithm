import sys

input = sys.stdin.readline

N = int(input())
N_list = list(map(int,input().split()))
M = int(input())
M_list = list(map(int,input().split()))

N_list.sort()

for i in M_list:
    start = 0
    end = N-1
    mid = N//2
    if i > N_list[-1] or i < N_list[0]:
        print(0)
    elif N_list[start] == i:
        print(1)
    elif N_list[end] == i:
        print(1)
    elif N_list[mid] == i:
        print(1)
    else:
        while start != end:
            if i == N_list[mid]:
                print(1)
                break
            elif i < N_list[mid]:
                end = mid
                mid = (start+end)//2
            else:
                start = mid+1
                mid = (start+end)//2
        else:
            if N_list[start] == i:
                print(1)
            else:
                print(0)