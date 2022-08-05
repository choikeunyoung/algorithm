import sys

sys.stdin = open("_민석이의과제체크하기.txt")

T = int(sys.stdin.readline())

for i in range(1,T+1):
    n,k = list(map(int,sys.stdin.readline().split()))
    num = list(map(int,sys.stdin.readline().split()))
    p_list = []
    for j in range(1,n+1):
        if j not in num:
            p_list.append(j)
    print(f"#{i}", end=' ')
    for k in p_list:
        print(k,end=' ')
    print()
