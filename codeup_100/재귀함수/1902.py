def N_print(n):
    if n == 0:
        return 0
    else:
        print(n)
        N_print(n-1)

N = int(input())

N_print(N)