import math

T = int(input())

for _ in range(T):
    num_list = list(map(int,input().split()))
    total = 0
    for i in range(1,len(num_list)-1):
        for j in range(i+1,len(num_list)):
            total += math.gcd(num_list[i],num_list[j])
    print(total)