import sys
T = int(sys.stdin.readline())
for i in range(1,T+1):
    num_dict = {}
    N = int(sys.stdin.readline())
    nums = list(map(int,sys.stdin.readline().split()))
    M = int(sys.stdin.readline())
    nums_check = list(map(int,sys.stdin.readline().split()))
    for j in nums:
        if j not in num_dict:
            num_dict[j] = 0

    for k in nums_check:
        if k in num_dict:
            print('1')
        else:
            print('0')