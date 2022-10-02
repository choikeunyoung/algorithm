N = int(input())

first_val = 666
count = 0
num_list = []
while True:
    new_val = first_val + count
    if "666" in str(new_val):
        num_list.append(new_val)
        if len(num_list) == N:
            print(num_list[-1])
    count += 1
