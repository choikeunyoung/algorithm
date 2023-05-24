import sys
# 인풋이 많기 떄문에 sys로 받는다
input = sys.stdin.readline

N=int(input())
# 숫자 리스트 생성
num_list = []
for _ in range(N):
    num_list.append(int(input()))
# 들어온 숫자를 오름차순 정렬
num_list.sort()
# check라는 변수로 순위를 1~N까지 하기때문에 1로 설정
check = 1
# 기대값과 순위 차이를 계산
total = 0
# num_list 안의 변수를 모두 순회
for i in num_list:
    # abs 사용하는 것보다 조건식으로 해결 큰값에서 작은값 빼도록
    if check > i:
        total += check - i
    else:
        total += i - check
    # 매 계산 후 등수 +1
    check += 1
print(total)