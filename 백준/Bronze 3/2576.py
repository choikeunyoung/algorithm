import sys

min_value = sys.maxsize
total = 0

for _ in range(7):
    num = int(input())
    if num % 2 == 1:
        total += num

    if num < min_value:
        min_value = num

if total == 0:
    print(-1)
else:
    print(total)
    print(min_value)
