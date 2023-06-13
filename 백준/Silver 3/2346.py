# 풍선 갯수
N = int(input())
# 풍선에 적힌 번호
num_list = list(map(int,input().split()))
# 풍선 번호와 인덱스 저장 리스트
check_list = []

for i,v in enumerate(num_list):
    check_list.append((v,i))
# 인덱스 번호
index = 0
# 리스트 길이 저장
list_length = len(num_list)
# 체크 리스트 존재하지 않을때 까지 반복문시행
while check_list:
    # 체크 변수에 리스트 인덱스 번호 추출
    check = check_list.pop(index)
    # 리스트 값이 -1 되서 길이 -1
    list_length -= 1
    # 리스트 길이를 먼저 -1 해주기 때문에 아래 연산이 맨 마지막 값에 대해서 0으로 나누기 때문에 0이면 1 넣어줌
    if list_length == 0:
        list_length = 1
    # 추출한 값이 양수인 경우 인덱스 번호는 -1을 해줘야 함으로 -1을 한 후  기존의 index 와 더한 후 리스트 길이보다 얼마나 클지 모르기 때문에 리스트 길이의 나머지를 구해줌
    if check[0] > 0:
        index = ((check[0] - 1) + index)%list_length
    # 음수인경우 인덱스와 그냥 더한 후 리스트 길이의 나머지를 구한다
    elif check[0] < 0:
        index = (check[0] + index)%list_length
    # 같이 넣어뒀던 인덱스 번호를 출력한다.
    print(check[1]+1, end=" ")