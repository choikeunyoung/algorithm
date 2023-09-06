N = int(input())
num_list = list(map(int, input().split()))
limit = int(input())
# 리스트 길이 체크
num_length = len(num_list)
cnt = 0
# limit 으로 들어온 값이 0 보다 크고 cnt 값이 num_length 보다 작을때 까지
while limit > 0 and cnt < num_length:
    # max_value 값을 num_list 슬라이싱을 통해서 cnt부터 cnt + limit + 1 과 num_length 보다 작은값까지
    max_value = max(num_list[cnt:min(cnt + limit + 1, num_length)])
    # max_value 의 인덱스를 cnt 부터 cnt + limit + 1 과 num_length 보다 작은 값까지
    max_index = num_list.index(max_value, cnt, min(cnt + limit + 1, num_length))
    # max_index 부터 cnt 까지 -1 씩 빼가며
    for j in range(max_index, cnt, -1):
        # j 값이 0보다 크고 num_list[j-1] 값이 num_list[j] 보다 작으면
        if j > 0 and num_list[j - 1] < num_list[j]:
            # 값 교체
            num_list[j - 1], num_list[j] = num_list[j], num_list[j - 1]
            # limit -1
            limit -= 1
        # 그 외의 경우 반복문 탈출
        else:
            break
    # cnt 값 연산마다 1씩 증가
    cnt += 1
    
print(*num_list)