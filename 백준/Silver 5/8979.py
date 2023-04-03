N,K = map(int,input().split())

num_list = []
# 나라별 리스트 추가
for _ in range(N):
    country = list(map(int,input().split()))
    num_list.append(country)
# 금, 은, 동 순으로 리스트 정렬
num_list.sort(reverse=True, key=lambda x:(x[1],x[2],x[3]))
# 내가 원하는 나라의 금 은 동 메달 갯수 저장
for i in range(N):
    if num_list[i][0] == K:
        check_list = num_list[i][1:]
# 반복문 순회하며 그 나라의 금, 은, 동 개수가 같은 인덱스값 출력
for j in range(N):
    if num_list[j][1:] == check_list:
        print(j+1)
        break