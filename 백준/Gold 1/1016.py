def prime_number(min_num , max_num):
    global cnt, left, right
    max_length = int(1000001000000**0.5)
    for i in range(2,max_length+1):
        if min_num <= i * i <= max_num:
            cnt += 1
        elif i * i > max_num:
            break


min_num, max_num = map(int,input().split())
cnt = 0
left = 0
right = 0
ans = prime_number(min_num, max_num)
print(max_num-min_num-cnt)