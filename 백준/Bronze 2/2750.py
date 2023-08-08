import sys
import heapq

num_list=[]
second_list=[]
for i in range(int(sys.stdin.readline())):
    heapq.heappush(num_list,int(sys.stdin.readline()))

while num_list:
    print(heapq.heappop(num_list))
    