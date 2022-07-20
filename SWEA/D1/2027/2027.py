l = ['#','+','+','+','+']
for j in range(0,len(l)-1):
    for i in range(0,len(l)):
        print(l[i],end="")
    print("")
    l[j+1] = l[j]
    l[j] = '+'
    if j == 3:
        for k in range(0,len(l)):
            print(l[k], end='')