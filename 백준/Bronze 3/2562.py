num = 0
cnt = 0
for i in range(9):
    x = int(input())
    if x > num:
        num = x
        cnt = i
print(num)
print(cnt+1)