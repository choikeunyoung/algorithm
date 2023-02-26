def prime_num(num):
    prime_list = [False, False] + [True]*num
    for i in range(2,num+1):
        if prime_list[i]:
            for j in range(2*i,num,i):
                prime_list[j] = False
    return list(x for x in range(2,num+1) if prime_list[x])

N = int(input())

prime_list = prime_num(N)
cnt = 0
while True:    
    if N == 1:
        break
    else:
        if N % prime_list[cnt] == 0:
            print(prime_list[cnt])
            N //= prime_list[cnt]
        else:
            cnt += 1