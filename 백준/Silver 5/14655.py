N = int(input())

first = list(map(int,input().split()))
second = list(map(int,input().split()))

first_max = 0
second_max = 0

for i in first:
    first_max += abs(i)

for i in second:
    second_max += abs(i)

print(first_max + second_max)