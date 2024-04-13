def prime_check():
    prime_list = [False, False] + [True]*10**7

    for i in range(2,(10**4)+1):
        if prime_list[i]:
            for j in range(i*2,(10**7)+1,i):
                prime_list[j] = False
    return prime_list
    

start, end = map(int,input().split())

cnt = 0
num_list = prime_check()

for i in range(int(start**.5), int(end**.5)+1):
    if num_list[i]:
        index = 2
        while i**index <= end:
            cnt += 1
            index += 1


print(cnt)