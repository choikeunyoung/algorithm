import sys

sys.stdin = open('input.txt', 'r')

T = int(sys.stdin.readline())

for i in range(1, T+1):
    cnt = 0
    j = str(i)
    a = 0
    for k in j:
        if k in '369':
            cnt+=1
            a = int(j)
    if i == a:
        print('-'*cnt, end=' ')
    else:
        print(i, end=' ')