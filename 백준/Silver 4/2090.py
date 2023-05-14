import math
# 리스트의 최소공배수를 구하는 함수
def euclid(nums):
    lcm = nums[0]
    check = 1
    for i in range(check,len(nums)):
        lcm = math.lcm(lcm,nums[i])
    return lcm

N = int(input())
num_list = list(map(int,input().split()))
# N값이 1인경우 그냥 수를 뒤집어주기만 하면된다.
if N == 1:
    print(num_list[-1],end="")
    print("/",end="")
    print(1)
# 그 외의 경우
else:
    # 최소공배수를 함수를 통해서 구한다.
    lcm = euclid(num_list)
    total = 0
    # 리스트를 반복해가며 최소공배수를 i값으로 나눠가며 값을 더해준다.
    for i in num_list:
        middle_value = lcm//i
        total += middle_value
    # 모두 계산을 끝냈을 경우 총합과 최소공배수가 나눠 떨어지는지 확인
    gcd = math.gcd(total,lcm)
    # 둘의 최대공약수를 나눠준다.
    lcm = lcm//gcd
    total = total//gcd
    print(lcm,end="")
    print("/",end="")
    print(total)