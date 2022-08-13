a = int(input())

if a % 12 == 0 or a % 12 == 1 or a % 12 == 2:
    print('winter')
elif a%12 == 3 or a%12 == 4 or a%12 == 5:
    print('spring')
elif a%12 == 6 or a%12 == 7 or a%12 == 8:
    print("summer")
else:
    print('fall')