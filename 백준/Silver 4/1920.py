import sys

input = sys.stdin.readline

N = int(input())
N_list = list(map(int,input().split()))
M = int(input())
M_list = list(map(int,input().split()))
# 이분 탐색을 위한 정렬
N_list.sort()
# 리스트 값들 반복문 처리
for i in M_list:
    # 시작은 0번 끝은 N-1 중간은 N//2
    start = 0
    end = N-1
    mid = N//2
    # 만약 i 값이 범위를 벗어난 경우 0 출력
    if i > N_list[-1] or i < N_list[0]:
        print(0)
    # 0번 인덱스 끝 인덱스 중간 인덱스값이랑 같은경우 1출력
    elif N_list[start] == i:
        print(1)
    elif N_list[end] == i:
        print(1)
    elif N_list[mid] == i:
        print(1)
    # 그 외의 경우
    else:
        # 시작값과 끝값이 같으면 계속 반복하기 때문에 그 전까지
        while start != end:
            # 만약 mid 값이랑 같은 경우 출력
            if i == N_list[mid]:
                print(1)
                break
            # 그 외의 경우 mid 값보다 작은 경우
            elif i < N_list[mid]:
                # end 자리에 mid 삽입 후 mid 값 조정
                end = mid
                mid = (start+end)//2
            # mid 값보다 큰 경우
            else:
                # 시작값을 mid +1 로 변경
                start = mid+1
                mid = (start+end)//2
        # break에 의한 종료가 아닌경우
        else:
            # start 랑 end 값이 동일하므로 start 인덱스 값과 같은 경우 1 출력 그 외의 경우 0
            if N_list[start] == i:
                print(1)
            else:
                print(0)