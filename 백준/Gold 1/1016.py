def prime_number(min_num , max_num):
    max_length = int(1000001000000**0.5)
    cnt = 0
    for i in range(2,max_length):
        end_value = max_length//(i*i)
        for j in range(i*i,end_value,i*i):
            print(j)
            if j <= max_num:
                if j >= min_num:
                    cnt += 1
            else:
                break
    return cnt

min_num, max_num = map(int,input().split())
check = prime_number(min_num, max_num)

print(max_num-min_num+1-check)