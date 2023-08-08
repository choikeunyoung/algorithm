import sys
import heapq

num_list=[]

for i in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    if N == 0:
        if len(num_list)==0:
            print(0)
        else:
            data = heapq.heappop(num_list)
            print(data[1])
    else:
        heapq.heappush(num_list, (abs(N),N))