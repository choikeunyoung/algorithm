def prime_num():
    F = [1]*1000001

    for i in range(2,int(1000000**0.5)+1):
        if F[i]:
            for j in range(i*2,1000001,i):
                F[j] = 0
    
    return F

prime_list = prime_num()

T = int(input())

for _ in range(T):
    num = int(input())
    cnt = 0
    for i in range(2,num//2+1):
        if prime_list[i] and prime_list[num-i]:
            cnt+=1
    print(cnt)