def factory(num):
    if num == 0:
        return 1
    else:
        return num * factory(num-1)

cnt = str(factory(int(input())))
check = 0

for i in cnt[::-1]:
    if i == '0':
        check += 1
    else:
        print(check)
        break