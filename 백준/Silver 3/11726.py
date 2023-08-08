import operator as op
from functools import reduce

# 조합의 개수 구하는 코드 => https://brownbears.tistory.com/459 출처
def nCr(n, r):
    if n == 1:
        return 1
    numerator = reduce(op.mul, range(n, n-r, -1), 1)
    denominator = reduce(op.mul, range(1, r+1), 1)
    return numerator // denominator

# 2
# ㅣㅣ = 

# 3 

# ㅣㅣㅣ 1개 ㅣ 1개 = 0 nCr 1개
# ㅣ= = ㅣ 2개 l 1개 = 1개 2C1  2개

# 5

# ㅣㅣㅣㅣㅣ l 1개 = 0 1C0 1개
# ㅣㅣㅣ =    ㅣ 3개 = 1개 4C1 4개



T = int(input())

total = 0
n = 0
quotient = T//2 # 9 4개  0~4개

for i in range(0,quotient+1):
    n = (T-2*i) + i
    total += nCr(n,i)
print(total%10007)