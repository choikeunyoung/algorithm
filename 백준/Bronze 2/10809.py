str_dict = {}
for i in range(97, 123):
    str_dict[chr(i)] = -1

check_str = input()

cnt = 0

for j in check_str:
    if str_dict[j] == -1:
        str_dict[j] = cnt
    else:
        pass
    cnt += 1

for k in str_dict.values():
    print(k, end=" ")