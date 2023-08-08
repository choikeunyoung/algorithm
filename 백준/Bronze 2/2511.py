A = list(map(int,input().split()))
B = list(map(int,input().split()))
A_sum = 0
A_cnt = 0
B_sum = 0
B_cnt = 0
total_cnt = 0

for i in range(len(A)):
    if A[i] > B[i]:
        A_sum += 3
        A_cnt = i
    elif A[i] < B[i]:
        B_sum += 3
        B_cnt = i
    else:
        A_sum += 1
        B_sum += 1
        total_cnt += 1

if A_sum > B_sum:
    print(A_sum, B_sum)
    print('A')
elif A_sum < B_sum:
    print(A_sum, B_sum)
    print('B')
else:
    if total_cnt == len(A):
        print(A_sum, B_sum)
        print('D')
    else:
        if A_cnt > B_cnt:
            print(A_sum, B_sum)
            print('A')
        elif A_cnt < B_cnt:
            print(A_sum, B_sum)
            print('B')