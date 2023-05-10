N = int(input())
M = int(input())
check_list = list(map(int,input().split()))
# 리스트 정렬
check_list.sort()
# 투 포인터에 사용할 0번 인덱스와 끝 인덱스
i = 0
j = N-1
cnt = 0
# 두 인덱스 위치가 교차할때 종료
while i < j:
    # 값을 더한게 M 보다 작으면 j는 이미 끝이기 때문에 작은 인덱스의 번호를 증가
    if check_list[i] + check_list[j] < M:
        i += 1
    # 같으면 카운트 증가하고 각각 위치를 한칸씩 옮김
    elif check_list[i] + check_list[j] == M:
        cnt += 1
        i += 1
        j -= 1
    # 더한 값이 더 큰 경우는 작은 값을 건들이는 것이 아닌 큰 값의 인덱스를 바꿔야함
    else:
        j -= 1
print(cnt)