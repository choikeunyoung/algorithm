T = int(input())

for i in range(1,T+1):
    info = list(map(str,input().split()))
    check_list=[]
    cnt = int(info[0])
    for j in info[1]:
        check_list.append(j)
    del check_list[cnt-1]
    for k in check_list:
        print(k,end="")
    print()