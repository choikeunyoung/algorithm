T = int(input())

for i in range(1,T+1):
    sum_list=[]
    check_list=[]
    a = list(input())
    
    for k in range(0,len(a)):
        if a[k] == 'O':
            check_list.append(1)
        else:
            check_list.append(0)

    for l in range(1, len(check_list)):
        if a[l-1] == 'O' and a[l] == 'O':
            check_list[l] += check_list[l-1]
    print(sum(check_list))

