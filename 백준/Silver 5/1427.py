# input을 문자열로 받아옴
N = input()
# 정렬한 리스트 생성
sort_list = []
# 문자열 한 단어마다
for i in N:
    # 리스트에 추가
    sort_list.append(int(i))
# 리스트 정렬
sort_list.sort()
# 정렬된 리스트 역순으로 출력
for j in sort_list[::-1]:
    print(j, end="")