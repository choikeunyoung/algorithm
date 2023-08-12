def counting(num):
    if num == 1:
        return 1
    elif num == 2:
        return 3
    else:
        return 2*counting(num-2) + counting(num-1)
   

T = int(input())

for tc in range(1, T+1):
    num = int(input())
    num = counting(num//10)
    print(f"#{tc} {num}")