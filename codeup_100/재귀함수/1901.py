def N_print(n):
    if n == 0:
        return 0
    else:
        print(N-(n-1))
        N_print(n-1)

N = int(input())

N_print(N)
