import sys

sys.stdin = open('input.txt', 'r')

t = sys.stdin.readline()
s = []
for i in t:
    print(ord(i)-64, end=' ')

# t = input()

# for i in t:
#     print(ord(i)-64, end=' ')


