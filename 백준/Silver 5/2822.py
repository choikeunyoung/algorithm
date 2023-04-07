num_list = []

cnt = 1
# 인풋값 8개 값들을 리스트 저장, 인덱스값까지
for _ in range(8):
    num_list.append([int(input()),cnt])
    cnt += 1
# 들어온 숫자를 내림차순으로 정렬
num_list.sort(reverse=True)
total = 0
# 상위 5개 점수의 합을 변수에 저장
for j in range(5):
    total += num_list[j][0]
# 총합 출력
print(total)
# 인덱스 리스트 생성
ans_list = []
# 인덱스 리스트에 상위 5개 인덱스 저장
for j in range(5):
    ans_list.append(num_list[j][1])
# 오름차순 정렬
ans_list.sort()
print(*ans_list)