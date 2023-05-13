import sys

input = sys.stdin.readline
# 들어오는 input의 갯수
N = int(input())
# 가격 리스트 생성
pay_list = []
# N만큼 리스트 반복
for _ in range(N):
    pay_list.append(int(input()))
# 리스트 역순 정렬
pay_list.sort(reverse=True)
# 총가격 변수
total_pay = 0
# 인덱스와 값을 순회하며 값을 더해나감 음수일 경우 이후로도 음수이기 때문에 break
for i,v in enumerate(pay_list):
    pay = v - i
    if pay >= 0:
        total_pay += pay
    else:
        break
print(total_pay)