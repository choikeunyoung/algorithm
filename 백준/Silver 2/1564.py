N = input()

max_length= len(N)

N = int(N)

ans = 1

for i in range(1,N+1):
    check = max_length
    if i % 5 == 0:
        while check != 0:
            five_value = 5*check
            if i % five_value == 0:
                i //= five_value
            else:
                check -= 1
    print(i)
    ans *= i

print(ans)