from re import I


x = int(input())
y = 0

for i in range(x+1):
    if i%2 == 0:
        y += i

print(y)