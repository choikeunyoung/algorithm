M = int(input())
cup_dict = {
    1 : 1,
    2 : 2,
    3 : 3
}

for i in range(M):
    a,b = map(int,input().split())
    x = cup_dict[a]
    y = cup_dict[b]
    cup_dict[a] = y
    cup_dict[b] = x

for k,v in cup_dict.items():
    if v == 1:
        print(k)