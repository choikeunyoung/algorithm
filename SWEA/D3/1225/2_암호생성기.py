import sys

sys.stdin = open("_암호생성기.txt")

for i in range(1,11):
    l = int(sys.stdin.readline())
    data = list(map(int,sys.stdin.readline().split()))
    cnt = 1
    temp = 0
    while True:
        temp = data[0]-cnt
        if cnt == 5:
            cnt = 0
        for j in range(len(data)-1):
            data[j] = data[j+1]
        data[len(data)-1] = temp
        cnt+=1
        if data[len(data)-1] <= 0:
            data[len(data)-1] = 0
            break
    print(f"#{i}", end=' ')
    for k in data:
        print(k,end=' ')
    print()