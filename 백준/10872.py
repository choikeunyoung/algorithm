def factory(num):
    if num == 0:
        return 1
    else:
        return num * factory(num-1)

print(factory(int(input())))