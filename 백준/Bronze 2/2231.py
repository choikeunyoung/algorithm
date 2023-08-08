N = int(input())
i = 1
k = 0
while i!=N:
    new_num = list(str(i))
    c = list(map(int,new_num))
    c = sum(c)
    k = i+c
    if k == N:
        break
    i+=1
if k == N:
    print(i)
else:
    print('0')
