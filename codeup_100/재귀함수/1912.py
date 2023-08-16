def fac(num):
    if num == 1:
        return 1
    else:
        return num * fac(num-1)

N = int(input())
print(fac(N))