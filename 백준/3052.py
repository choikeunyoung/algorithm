T = []
for i in range(0,10):
    T.extend(list(map(int,input().split())))

T_dict={}

for j in T:
    k = j%42

    if k in T_dict:
        T_dict[k] += 1
    else:
        T_dict[k] = 1
print(len(list(T_dict)))