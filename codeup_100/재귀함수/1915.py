def fibo(num):
    if num == 1:
        return 1
    elif num == 0:
        return 0
    else:
        return fibo(num-2) + fibo(num-1)

N = int(input())
print(fibo(N))