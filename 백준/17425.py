import sys

# 미리 연산으로 약수와 약수의 합을 가져와서 연산한다 => 메모리 사용이 많기 때문에 풀때 메모리를 많이 사용하는지 확인해보기

def test():
    num_dict = {}
    for i in range(1,10000001):
        j = 0
        for k in range(1,i+1):
            j += (k*(i//k))
        print(j)
    return num_dict

print(test())

# stdin = sys.stdin.readline

# T = int(stdin())

# for _ in range(T):
#     N = int(stdin())
#     print(test(N))