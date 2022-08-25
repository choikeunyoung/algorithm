N = int(input())
dict = {}
for _ in range(N*2-1):
    names = input()
    if _ <= N-1:
        if names in dict:
            dict[names] += 1
        else:
            dict[names] = 1
    else:
        if names in dict:
            dict[names] -= 1

for k,v in dict.items():
    if v > 0:
        print(k)