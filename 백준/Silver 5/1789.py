S = int(input())
s = S*2
print(s)
n = int(1)

while True:
    if s < n*(n+1):
        print(n-1)
        break
    elif s == n*(n+1):
        print(n)
        break
    else:
        n += 1