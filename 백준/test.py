A_card = []
B_card = []
for i in range(2):
    card_num = list(map(int, input().split()))
    if i == 0:
        A_card = card_num
    if i == 1:
        B_card = card_num

A_point = 0
B_point = 0
check_list = []
for j in range(10):
    if A_card[j] > B_card[j]:
        A_point += 3
        check_list.append("A")
    if A_card[j] < B_card[j]:
        B_point += 3
        check_list.append("B")
    if A_card[j] == B_card[j]:
        A_point += 1
        B_point += 1
        check_list.append("D")

print(A_point, B_point)
if check_list.count("D") == 10:
    print("D")
else:
    if A_point > B_point:
        print("A")
    if B_point > A_point:
        print("B")
    if (A_point == B_point) and (check_list[-1] == "D"):
        for i in check_list[::-1]:
            if i == "D":
                continue
            if i != "D":
                print(i)
                break