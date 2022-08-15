a, b, c = map(int,input().split())
num = 1
while num%a != 0 or num%b != 0 or num%c != 0:
    num += 1

print(num)