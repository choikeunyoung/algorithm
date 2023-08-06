first_list = []
second_list = []

for _ in range(4):
    first_list.append(int(input()))

for _ in range(2):
    second_list.append(int(input()))

first_list.sort(reverse=True)

total = sum(first_list[:3])
print(total + max(second_list))
