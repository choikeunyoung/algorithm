x = int(input())
y = 0
z = 1
while True:
    y = y + z
    if y >= x:
        print(z)
        break
    else:
        z=z+1