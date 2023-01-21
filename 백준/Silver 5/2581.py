def prime(n,m):
    prime_list = [False, False] + [True]*10**4
    num_list = []
    for i in range(1,10001):
        if prime_list[i]:
            for j in range(i*2,10001,i):
                prime_list[j] = False
    for x in range(n,m+1):
        if prime_list[x]:
            num_list.append(x)

    return num_list

n = int(input())
m = int(input())
prime_num = prime(n,m)
if not len(prime_num):
    print(-1)
else:
    print(sum(prime_num))
    print(prime_num[0])