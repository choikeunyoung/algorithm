import sys
T = int(sys.stdin.readline())
for i in range(1,T+1):
    N = int(sys.stdin.readline())
    nums = list(map(int,sys.stdin.readline().split()))
    M = int(sys.stdin.readline())
    nums_check = list(map(int,sys.stdin.readline().split()))
    for j in nums_check:
        if j in nums:
            print('1')
        else:
            print('0')