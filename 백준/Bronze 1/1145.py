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

# import math
# nums = list(map(int,input().split()))

# nums.sort()
# for i in range(2,nums[-1]+1):
#     cnt = 0
#     check_list = []
#     for j in nums:
#         if j%i == 0:
#             if cnt == 3:
#                 break
#             else:
#                 cnt += 1
#                 check_list.append(j)
#     if cnt == 3:
#         print(math.lcm(check_list[0], check_list[1], check_list[2]))
#         break

