import math

nums = list(map(int,input()))
number = ""
answer = 1

for i in nums:
    answer = math.lcm(answer,i)
    number += str(i)
    
number_length = len(number)
number = int(number)
limit = 10**9 // answer
for i in range(1, limit+1):
    check = i*answer
    if check >= number:
        if n