import sys

sys.stdin = open('input.txt', 'r')

T = int(sys.stdin.readline())
# 1은 가위
# 2는 바위
# 3은 보
for i in range(1,T+1):
    a,b=map(int,sys.stdin.readline().split())
    if a == 1 and b == 2:
        print("B")
    elif a == 1 and b == 3:
        print("A")
    elif a == 2 and b == 1:
        print("A")
    elif a == 2 and b == 3:
        print("B")
    elif a == 3 and b == 1:
        print("B")
    elif a == 3 and b == 2:
        print("A")

# a,b = map(int,input().split())

# if a == 1 and b == 2:
#     print("B")
# elif a == 1 and b == 3:
#     print("A")
# elif a == 2 and b == 1:
#     print("A")
# elif a == 2 and b == 3:
#     print("B")
# elif a == 3 and b == 1:
#     print("B")
# elif a == 3 and b == 2:
#     print("A")