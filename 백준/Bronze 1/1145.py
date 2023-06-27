import math
import sys

num_list = list(map(int,input().split()))
answer = sys.maxsize

for i in range(5):
    for j in range(i+1,5):
        for k in range(j+1,5):
            total = math.lcm(num_list[i],num_list[j],num_list[k])
            if total < answer:
                answer = total
print(answer)