# N, num_list, x 값을 받는 부분
N = int(input())
num_list = list(map(int,input().split()))
x = int(input())
# num_list 를 탐색하기 위해서 오름차순 정렬
num_list.sort()
# 갯수 체크, 시작점, 끝점 체크
cnt = 0
start = 0
end = N-1
# start 값이 end 값보다 크면 탈출
while start < end:
    # answer 변수에 시작과 끝의 부분부터 탐색 시작
    answer = num_list[start] + num_list[end]
    # 만약 정답이 x보다 작으면 왼쪽 값을 1씩 증가
    if answer < x:
        start += 1
    # 정답이 x보다 크면 오른쪽 값을 1씩 감소
    elif answer > x:
        end -= 1
    # 정답인 경우 무한루프 탈출을 위해 큰값을 -1씩 후 cnt 증가
    else:
        cnt += 1
        end -=1
print(cnt)