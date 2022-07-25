T = int(input())

if T%4 == 0 and T%100 != 0 or T%400 == 0:
    print("1")
else:
    print("0")