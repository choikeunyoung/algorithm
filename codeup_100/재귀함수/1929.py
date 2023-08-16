def right_park_soo(num):
    if num == 1:
        return
    if num % 2 == 1:
        num = (3*num + 1)
        right_park_soo(num)
    else:
        num //= 2
        right_park_soo(num)
    print(num)



N = int(input())

right_park_soo(N)
print(N)