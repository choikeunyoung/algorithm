from operator import itemgetter, attrgetter
import sys

input = sys.stdin.readline

N = int(input())

num_list = []

for _ in range(N):
    x,y = map(int,input().split())
    num_list.append((x,y))


num_list.sort(key = lambda x: (x[1], x[0]))

for i in range(N):
    print(num_list[i][0], num_list[i][1])