from itertools import count


for i in range(1,10001):
    for j in range(1,i):
        if j < 10:
            k = j + j%10
            if k == i:
                break
            else:
                print(i)
        elif j < 100:
            k = j + j//10 + j%10
            if k == i:
                break
            else:
                print(i)