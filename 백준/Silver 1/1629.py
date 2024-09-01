def divide(value, target, other):
    if target == 1:
        return value % other
    else:
        temp = divide(value, target // 2, other)
        if target % 2 == 0:
            return (temp * temp) % other
        else:
            return (temp * temp * value) % other


A, B, C = map(int, input().split())
print(divide(A, B, C))
