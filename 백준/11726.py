import operator as op
from functools import reduce

# 조합의 개수 구하는 코드 => https://brownbears.tistory.com/459 출처
def nCr(n, r):
    if n == 1:
        return 1
    numerator = reduce(op.mul, range(n, n-r, -1), 1)
    denominator = reduce(op.mul, range(1, r+1), 1)
    return numerator // denominator



T = int(input())

total = 0
n = 0
quotient = T//2

for i in range(0,quotient+1):
    n = (T-2*i) + i
    total += nCr(n,i)
print(total%10007)