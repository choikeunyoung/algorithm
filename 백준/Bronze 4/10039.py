total = 0
for _ in range(5):
    num = int(input())
    if num < 40:
        num = 40
        total += num
    else:
        total += num
print(total // 5)
