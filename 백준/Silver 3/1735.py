import math
# 분수로 나타낼 수들을 각각 input 으로 받아온다
A,B = map(int,input().split())
C,D = map(int,input().split())
# 분모의 최소공배수를 구한다
lcm = math.lcm(B,D)
# 분자에 각각 분모의 최소공배수에서 기존의 분모를 나눈 몫을 곱해준다
A = A*(lcm//B)
C = C*(lcm//D)
# 두 분자의 합을 구한다
total = A+C
# 분자와 분모가 약분이 되는지 확인
gcd = math.gcd(total,lcm)
# 분자와 분모의 최대공약수로 나눠준다.
print(total//gcd,lcm//gcd)