import sys

input = sys.stdin.readline

N = int(input())
# sys.maxsize 사용할 경우 python 에서 낼 수 있는 최대값을 불러올 수 있다고 한다.
min_value = sys.maxsize
max_value = -sys.maxsize
# 모든 값들을 더해줄 변수
total = 0
# 들어온 숫자 딕셔너리로 몇개 들어왔는지 카운트
num_dict  = {}
# 들어온 숫자들 리스트
check_list = []
# 최빈값 구하기 위한 리스트
num_list = []

for _ in range(N):
    num = int(input())
    # 들어온 값이 max_value 와 비교해서 크면 값을 덮어 씌움
    if max_value < num:
        max_value = num
    # 똑같이 min_value 와 비교해서 작으면 덮어 씌움
    if min_value > num:
        min_value = num
    # 들어온 값을 더해줌
    total += num
    # 딕셔너리안에 있으면 value 값을 +1 없으면 추가
    if num in num_dict:
        num_dict[num] += 1
    else:
        num_dict[num] = 1
    # 숫자들 리스트에 저장
    check_list.append(num)

# 숫자들 정렬
check_list.sort()
# 딕셔너리 value 값중 최빈값 저장
max_count = max(num_dict.values())
# 딕셔너리를 순회하며 value 값이 1이 아니면서 max_count 랑 같은경우 최빈값 리스트에 값저장
for k,v in num_dict.items():
    if v == max_count and v != 1:
        num_list.append(k)
# python round는 오사오입을 적용하지만 앞자리가 홀수냐 짝수냐에 따라서 결과가 달라진다.
# 앞의 자리가 짝수인지 홀수인지 체크해주는 변수 생성
check_avg = total/N

# 앞자리가 짝수인 경우 홀수로 만들어서 반올림한 후 +1
if (check_avg//1)%2 ==0:
    check_avg = round(check_avg-1)+1
else:
    check_avg = round(check_avg)

# 최빈값이 2개이상인 경우 num_list를 정렬한 후 2번째 값 출력
if len(num_list) > 1:
    num_list.sort()
    print(check_avg)
    print(check_list[N//2])
    print(num_list[1])
    print(max_value-min_value)
else:
    print(check_avg)
    print(check_list[N//2])
    # num_list 값이 0 인 경우
    if len(num_list) == 0:
        # N 이 1이 아니면 check_list에서 2번째 값을 출력 => 문제에서 요구한 것
        if N != 1:
            print(check_list[1])
        # 그 외의 경우 0이나 -1 출력 같기때문
        else:
            print(check_list[-1])
    # num_list 길이가 1인 경우 0번째 인덱스 출력
    else:
        print(num_list[0])
    print(max_value-min_value)