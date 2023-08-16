def sum_num(n):
    if n == 1:
        return 1
    else:
        return n + sum_num(n-1)

N = int(input())

print(sum_num(N))