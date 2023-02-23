import sys

input = sys.stdin.readline

N = int(input())
# 배열의 인덱스를 카운트할 변수
index = 0
# 배열을 저장할 리스트
info_list = []
# 배열을 임시로 저장할 리스트
infos = []
for _ in range(N):
    # 들어온 값을 임시 리스트에 저장
    infos = list(map(str,input().split()))
    # 임시 리스트에 인덱스 추가
    infos.append(index)
    # 배열 리스트에 임시 리스트 값 추가
    info_list.append(infos)
    # 인덱스 값 증가
    index += 1
# 배열 리스트를 정렬하는데 문자열로 입력받았기 때문에 숫자로 바꾼 후 0번을 기준으로 같을경우 먼저 들어온 경우로 정렬
info_list.sort(key= lambda x:(int(x[0]),x[2]))
for i in info_list:
    print(i[0],i[1])