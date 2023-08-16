def even_num(n, m):
    if n == m+1:
        return 0
    else:
        if n % 2 == 1:
            print(n, end=" ")
        even_num(n+1, m)

N, M = map(int,input().split())

even_num(N,M)
