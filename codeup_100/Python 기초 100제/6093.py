n = int(input())
list = list(map(int,input().split()))
for i in range(len(list)-1,-1,-1):
    print(list[i], end = ' ')