def right_park_soo(num):
    print(num)
    if num == 1:
        return num
    if num % 2 == 1:
        right_park_soo(3*num + 1)
    else:
        right_park_soo(num//2)



N = int(input())

right_park_soo(N)