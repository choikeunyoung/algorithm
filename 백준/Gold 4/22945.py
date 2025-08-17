N = int(input())

num_list = list(map(int,input().split()))
# 시작점
start = 0
# 끝점
end = N-1
# 최대 값 체크
max_value = 0
# 시작값보다 끝값이 작아질때까지
while start < end:
    # 문제 조건에 따른 공식 적옹
    value = (end - start - 1) * min(num_list[start],num_list[end])
    # 최대값 갱신
    if max_value < value:
        max_value = value
    # 포인터 위치 변경 조건
    if num_list[start] < num_list[end]:
        start += 1
    else:
        end -= 1

print(max_value)