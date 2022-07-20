import sys

sys.stdin = open('input.txt', 'r')

T = int(sys.stdin.readline())
total = 0
for i in range(1,T+1):
    val = int(sys.stdin.readline())
    for j in range(1, val+1):
        if j % 2 ==1:
            total += j
        else:
            total -= j
    print(total)
    total=0

# T = int(input())
# total = 0
# for i in range(1,T+1):
#     val = int(input())
#     for j in range(1, val+1):
#         if j % 2 ==1:
#             total += j
#         else:
#             total -= j
#     print(f"#{i}", total)
#     total=0
