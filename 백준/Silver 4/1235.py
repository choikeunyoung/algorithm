import sys

input = sys.stdin.readline

N = int(input())

num_list = []

for _ in range(N):
    num_list.append(input().strip())
# 문자의 길이를 받아올 변수 생성 => 몇자리 수까지 존재하는지 확인
total_length = len(num_list[0])
# 문자열 슬라이싱을 위해 1부터 맨마지막숫자까지
for i in range(1,total_length+1):
    # 체크해줄 변수생성
    flag = 0
    # 딕셔너리 생성하여 매 딕셔너리마다 값 체크
    ans_list = {}
    for j in num_list:
        # 숫자 리스트의 뒷부분부터 슬라이싱 시작하며 딕셔너리에 존재여부 확인
        if j[total_length-i:] in ans_list:
            ans_list[j[total_length-i:]] += 1
        else:
            ans_list[j[total_length-i:]] = 1
    # 딕셔너리 value 값중 v가 1보다 큰 경우 flag 체크 변수에 1을 넣어줌
    for v in ans_list.values():
        if v > 1:
            flag = 1
            break
    # flag 가 2이상인 경우 같은 값이 한개라도 존재하는 것이므로 그 외의 경우를 체크
    if flag != 1:
        print(i)
        break