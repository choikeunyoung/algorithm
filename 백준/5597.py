num_list = []


for j in range(28):
    a = int(input())
    num_list.append(str(a))

for i in range(1,31):
    if str(i) in num_list:
        pass
    else:
        print(i)