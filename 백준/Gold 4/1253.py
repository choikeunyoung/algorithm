N = int(input())
# 이분 탐색
num_list = list(map(int,input().split()))
# 정렬
num_list.sort()
cnt = 0

for i in range(N):
    # 시작
    start = 0
    # 끝
    end = N-1
    # 이분 탐색 진행
    while start < end:
        # 시작 인덱스와 끝 인덱스 합이 i 인덱스와 같은 경우
        if num_list[start] + num_list[end] == num_list[i]:
            # 서로 다른 두 수이기 때문에 i 면 안됨
            if start != i and end == i:
                # end 값이 i 랑 같으면 end -1
                end -=1
            elif start == i and end != i:
                # start 값이 i 랑 같으면 start +1
                start += 1
            # 외의 경우 서로 다른 두수이므로 cnt 증가 후 탈출
            else:
                cnt += 1
                break
        # 값의 합이 큰 경우 end -1
        elif num_list[start] + num_list[end] > num_list[i]:
            end -= 1
        # 값의 합이 작은 경우 start +1
        elif num_list[start] + num_list[end] < num_list[i]:
            start += 1

print(cnt)