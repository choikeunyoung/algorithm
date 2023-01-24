num_list = list(map(int,input().split()))

total = 0

for i in num_list:
    total += i*i
print(total%10)