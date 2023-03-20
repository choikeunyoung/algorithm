# 집합 S 길이
S = int(input())
# 집합 S 리스트
num_list = list(map(int,input().split()))
# 찾을 숫자
n = int(input())
# 정렬부터 시작
num_list.sort()
# 만약 끝의 값보다 크거나 같은 경우
if n >= num_list[-1]:
    # 끝의 값과 n 이 같은 경우
    if n == num_list[-1]:
        print(0)
    # 그 외의 경우
    else:
        print((1000-n)*(n-num_list[-1])-1)
# 시작 값보다 작거나 같은 경우
elif n <= num_list[0]:
    # 시작값과 같은 경우
    if n == num_list[0]:
        print(0)
    else:
        print((num_list[0]-n)*(n)-1)
# 위 상황을 제외한 값들
else:
    # 1부터 리스트 길이만큼 반복문 시행
    for i in range(1,len(num_list)):
        # 한칸 큰 값을찾았을 경우
        if n < num_list[i]:
            print((num_list[i]-n)*(n-num_list[i-1])-1)
            break
        # 만약 값으 같은 경우
        elif n == num_list[i]:
            print(0)
            break