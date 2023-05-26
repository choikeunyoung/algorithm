# 조합을 위한 팩토리얼 함수 ( 재귀 )
def factorial(num):
    if num == 1:
        return 1
    else:
        return num*factorial(num-1)

N,M = map(int,input().split())

print(factorial(N)//(factorial(M)*factorial(N-M)))