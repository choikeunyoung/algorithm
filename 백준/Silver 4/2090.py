import math

def euclid(nums):
    lcm = nums[0]
    check = 1
    for i in range(check,len(nums)):
        lcm = math.lcm(lcm,nums[i])
    return lcm

N = int(input())
num_list = list(map(int,input().split()))
num_list.sort()
if N == 1:
    print("{}/{}".format(num_list[-1],1))
else:
    lcm = euclid(num_list)
    total = 0
    for i in num_list:
        middle_value = lcm//i
        total += middle_value
    print("{}/{}".format(lcm,total))